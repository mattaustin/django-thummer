# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from . import views


try:
    from django.urls import path_re
except ImportError:
    from django.conf.urls import url as path_re


app_label = 'thummer'


urlpatterns = [

    path_re(r'^(?P<width>\d+)/(?P<height>\d+)/(?P<crop>0|1)/(?P<scheme>https?)://?(?P<hierarchical_part>.*)$',  # noqa: E501
            views.ThumbnailView.as_view(), name='thumbnail'),

]
