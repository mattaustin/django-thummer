# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from celery.task import task


@task()
def capture(pk):
    from thummer.models import WebpageSnapshot
    instance = WebpageSnapshot.objects.get(pk=pk)
    instance._capture()

