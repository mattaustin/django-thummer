# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.core.files.storage import default_storage


STORAGE = getattr(settings, 'THUMMER_STORAGE', default_storage)

VALID_FOR = getattr(settings, 'THUMMER_SNAPSHOTS_VALID_FOR',
    relativedelta(months=+3))

UPLOAD_PATH = getattr(settings, 'THUMMER_UPLOAD_PATH', 'thummer/snapshots')

THUMBNAIL_DEFAULTS = getattr(settings, 'THUMMER_THUMBNAIL_DEFAULTS',
    {'crop': 'left top', 'upscale': False, 'format': 'JPEG'})

PLACEHOLDER_PATH = getattr(settings, 'THUMMER_PLACEHOLDER_PATH',
    'thummer/placeholder.png')

PLACEHOLDER_DEFAULTS = getattr(settings, 'THUMMER_PLACEHOLDER_DEFAULTS',
    {'crop': 'center', 'upscale': False, 'format': 'PNG'})

CELERY = 'djcelery' in settings.INSTALLED_APPS

QUEUE_SNAPSHOTS = CELERY and getattr(settings, 'THUMMER_QUEUE_SNAPSHOTS', True)

STATICFILES_STORAGE = settings.STATICFILES_STORAGE

