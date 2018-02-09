# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


try:
    from celery import shared_task
except ImportError:
    from functools import wraps

    # Faux shared_task decorator
    def shared_task(*args, **kwargs):
        def factory(func):
            @wraps(func)
            def decorator(*args, **kwargs):
                return func(*args, **kwargs)
            return decorator
        return factory


@shared_task(ignore_result=True)
def capture(pk):
    from .models import WebpageSnapshot
    instance = WebpageSnapshot.objects.get(pk=pk)
    return instance._capture()
