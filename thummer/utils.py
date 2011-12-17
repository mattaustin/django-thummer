# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from thummer.models import WebpageSnapshot


def get_thumbnail(url, geometry_string, **kwargs):
    """Finds or creates a valid ``WebpageSnapshot`` for the provided url,
    and returns its ``get_thumbnail`` method with the arguments provided."""
    try:
        webpage_snapshot = WebpageSnapshot.objects.filter(
            url=url).valid().latest()
    except WebpageSnapshot.DoesNotExist:
        webpage_snapshot = WebpageSnapshot(url=url)
    return webpage_snapshot.get_thumbnail(geometry_string, **kwargs)

