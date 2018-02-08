# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from datetime import datetime

from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.core.files.images import ImageFile
from django.core.files.storage import get_storage_class
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from sorl.thumbnail import get_thumbnail as sorl_thumbnail
from sorl.thumbnail import ImageField

from . import querysets, settings, tasks, utils

try:
    from hashlib import md5
except ImportError:
    from md5 import new as md5


@python_2_unicode_compatible
class WebpageSnapshot(models.Model):
    """Model representing a webpage snapshot."""

    url = models.URLField(db_index=True)

    image = ImageField(editable=False, storage=settings.STORAGE,
                       upload_to=settings.UPLOAD_PATH, null=True)

    capture_width = models.IntegerField(default=1680, editable=False)

    created_at = models.DateTimeField(editable=False, auto_now_add=True)

    captured_at = models.DateTimeField(editable=False, null=True)

    objects = querysets.WebpageSnapshotQuerySet.as_manager()

    class Meta(object):
        get_latest_by = 'captured_at'
        ordering = ['-captured_at']

    def __str__(self):
        return self.url

    def _capture(self):
        """Save snapshot image of webpage, and set captured datetime."""
        from selenium import webdriver
        from selenium.webdriver.firefox.options import Options
        options = Options()
        options.add_argument('--headless')
        browser = webdriver.Firefox(options=options)
        # browser.set_page_load_timeout(10)  # TODO
        capture_resolution = self._get_capture_resolution()
        browser.set_window_size(*capture_resolution)
        browser.get(self.url)
        viewport_height = browser.execute_script(
            'return document.body.scrollHeight;')
        browser.set_window_size(capture_resolution[0], viewport_height)  # TODO
        self.captured_at = datetime.now()
        png = browser.get_screenshot_as_png()

        browser.quit()
        self.image.save(self._generate_filename(), ContentFile(png))
        return True

    def _generate_filename(self):
        """Returns a unique filename base on the url and created datetime."""
        if not self.captured_at:
            raise ValidationError(
                'Cannot generate a filename when captured_at is not set.')
        hexdigest = md5(
            '{url}|{timestamp}'.format(
                url=self.url, timestamp=self.captured_at.isoformat()).encode(
                'utf-8')).hexdigest()
        return '{}/{}.png'.format(settings.UPLOAD_PATH, hexdigest)

    def _get_capture_resolution(self):
        return self.capture_width, int((self.capture_width/16.0)*10)

    def get_absolute_url(self):
        return self.image and self.image.url

    def get_image(self):
        return self.image or self.get_placeholder_image()

    def get_placeholder_image(self):
        storage_class = get_storage_class(settings.STATICFILES_STORAGE)
        storage = storage_class()
        placeholder = storage.open(settings.PLACEHOLDER_PATH)
        image = ImageFile(placeholder)
        image.storage = storage
        return image

    def get_thumbnail(self, geometry_string, **kwargs):
        """A shortcut for sorl thumbnail's ``get_thumbnail`` method."""
        for key, value in settings.THUMBNAIL_DEFAULTS.items():
            kwargs.setdefault(key, value)
        if not self.image:
            # Placeholder images
            kwargs.update(settings.PLACEHOLDER_DEFAULTS)
        if geometry_string is None:
            # We have to use django's ImageFile, as sorl-thumbnail's ImageField
            # extends File and not ImageFile, so width property is not
            # available.
            image = ImageFile(self.get_image().file)
            geometry_string = '{}'.format(image.width)
        return sorl_thumbnail(self.get_image(), geometry_string,  **kwargs)

    def save(self, *args, **kwargs):
        new = not self.pk
        super(WebpageSnapshot, self).save(*args, **kwargs)
        if new:
            if settings.QUEUE_SNAPSHOTS:
                tasks.capture.delay(pk=self.pk)
            else:
                tasks.capture(pk=self.pk)

models.signals.pre_delete.connect(utils.delete_image, sender=WebpageSnapshot)
