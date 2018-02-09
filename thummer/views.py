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

from django.http import HttpResponseRedirect
from django.views.generic import View

from .utils import get_thumbnail


class ThumbnailView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(self.get_thumbnail().url)

    def get_crop(self):
        return self.kwargs['crop'] == '1'

    def get_geometry_string(self):
        width = self.kwargs['width'] != '0' and self.kwargs['width'] or None
        height = self.kwargs['height'] != '0' and self.kwargs['height'] or None
        geometry_string = width
        if height is not None:
            geometry_string = '{}x{}'.format(geometry_string or '', height)
        return geometry_string

    def get_url(self):
        return '{scheme}://{hierarchical_part}'.format(
            scheme=self.kwargs['scheme'],
            hierarchical_part=self.kwargs['hierarchical_part'])

    def get_thumbnail(self):
        if self.get_crop():
            return get_thumbnail(self.get_url(), self.get_geometry_string())
        else:
            return get_thumbnail(self.get_url(), self.get_geometry_string(),
                                 crop='')
