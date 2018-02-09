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
