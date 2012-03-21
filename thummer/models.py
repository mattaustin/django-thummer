# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from datetime import datetime
from django.core.files.base import ContentFile
from django.db import models
from pyvirtualdisplay import Display
from selenium import webdriver
from sorl.thumbnail import ImageField, get_thumbnail as sorl_thumbnail
from thummer import settings, utils
from thummer.managers import QuerySetManager
import base64

try:
    from hashlib import md5
except ImportError:
    from md5 import new as md5


class WebpageSnapshot(models.Model):
    """Model representing a webpage snapshot."""
    url = models.URLField(db_index=True)
    image = ImageField(editable=False, storage=settings.STORAGE,
        upload_to=settings.UPLOAD_PATH)
    capture_width = models.IntegerField(default=1680, editable=False)
    created_at = models.DateTimeField(editable=False)
    objects = QuerySetManager()
    
    class QuerySet(models.query.QuerySet):
        def valid(self):
            created_after = datetime.now() - settings.VALID_FOR
            return self.filter(created_at__gte=created_after)
    
    def __unicode__(self):
        return self.url
    
    def _capture(self):
        """Save snapshot image of webpage, and set created datetime."""
        display = Display(visible=0, size=self._get_capture_resolution())
        display.start()
        browser = webdriver.Firefox()
        browser.get(self.url)
        self.created_at = datetime.now()
        png = browser.get_screenshot_as_base64()
        browser.quit()
        display.stop()
        self.image.save(self._generate_filename(),
            ContentFile(base64.decodestring(png)))
        return True
    
    def _generate_filename(self):
        """Returns a unique filename base on the url and created datetime."""
        assert self.created_at
        datetime_string = unicode(self.created_at)
        hexdigest = md5(datetime_string + self.url).hexdigest()
        return '%s/%s.png' %(settings.UPLOAD_PATH, hexdigest)
    
    def _get_capture_resolution(self):
        return (self.capture_width, int((self.capture_width/16.0)*10))
    
    def get_absolute_url(self):
        return self.image and self.image.url
    
    def get_image(self):
        if not self.image:
            self._capture()
        return self.image
    
    def get_thumbnail(self, geometry_string, **kwargs):
        """A shortcut for sorl thumbnail's ``get_thumbnail`` method."""
        kwargs.setdefault('crop', 'left top')
        return sorl_thumbnail(self.get_image(), geometry_string,  **kwargs)
    
    class Meta(object):
        get_latest_by = 'created_at'
        ordering = ['-created_at']

models.signals.pre_delete.connect(utils.delete_image, sender=WebpageSnapshot)

