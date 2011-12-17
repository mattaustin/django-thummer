# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.core.files.storage import default_storage


MEDIA_ROOT = getattr(settings, 'THUMMER_MEDIA_ROOT', settings.MEDIA_ROOT)

STORAGE = getattr(settings, 'THUMMER_STORAGE', default_storage)

VALID_FOR = getattr(settings, 'THUMMER_SNAPSHOTS_VALID_FOR',
    relativedelta(months=+3))

UPLOAD_PATH = getattr(settings, 'THUMMER_UPLOAD_PATH', 'thummer/snapshots')

