# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


__title__ = 'django-thummer'
__url__ = 'https://github.com/mattaustin/django-thummer'
__version__ = '3.0.dev1'


def get_thumbnail(*args, **kwargs):
    from .utils import get_thumbnail
    return get_thumbnail(*args, **kwargs)
