# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


try:
    from celery.task import task
except ImportError:
    from functools import wraps

    # Faux task decorator
    def task(*args, **kwargs):
        def factory(func):
            @wraps(func)
            def decorator(*args, **kwargs):
                return func(*args, **kwargs)
            return decorator
        return factory


@task(ignore_result=True)
def capture(pk):
    from .models import WebpageSnapshot
    instance = WebpageSnapshot.objects.get(pk=pk)
    instance._capture()
