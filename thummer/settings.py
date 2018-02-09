# -*- coding: utf-8 -*-
#
# Copyright 2011-2018 Matt Austin
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import absolute_import, unicode_literals

from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.core.files.storage import default_storage


try:
    import celery
except ImportError:
    CELERY = False
else:
    from . import tasks  # noqa: F401
    CELERY = 'thummer.tasks.capture' in celery.current_app.tasks.keys()


DEFAULT_CAPTURE_WIDTH = getattr(settings, 'THUMMER_DEFAULT_CAPTURE_WIDTH',
                                1280)

STORAGE = getattr(settings, 'THUMMER_STORAGE', default_storage)

VALID_FOR = getattr(settings, 'THUMMER_SNAPSHOTS_VALID_FOR',
                    relativedelta(months=+3))

UPLOAD_PATH = getattr(settings, 'THUMMER_UPLOAD_PATH', 'thummer/snapshots')

THUMBNAIL_DEFAULTS = getattr(settings, 'THUMMER_THUMBNAIL_DEFAULTS',
                             {'crop': 'left top', 'upscale': False,
                              'format': 'JPEG'})

PLACEHOLDER_PATH = getattr(settings, 'THUMMER_PLACEHOLDER_PATH',
                           'thummer/placeholder.png')

PLACEHOLDER_DEFAULTS = getattr(settings, 'THUMMER_PLACEHOLDER_DEFAULTS',
                               {'crop': 'center', 'upscale': False,
                                'format': 'PNG'})

QUEUE_SNAPSHOTS = CELERY and getattr(settings, 'THUMMER_QUEUE_SNAPSHOTS', True)

STATICFILES_STORAGE = settings.STATICFILES_STORAGE
