# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls.defaults import include, patterns, url
from thummer.views import ThumbnailView


urls = patterns(

    'thummer.views',

    url(r'^(?P<width>\d+)/(?P<height>\d+)/(?P<crop>0|1)/(?P<scheme>https?)://?(?P<hierarchical_part>.*)$',  # noqa: E501
        ThumbnailView.as_view(), name='thumbnail'),

)

urlpatterns = patterns('', url(r'^', include(urls, namespace='thummer')))
