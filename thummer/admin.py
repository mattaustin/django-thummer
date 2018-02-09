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

from django.contrib import admin

from .models import WebpageSnapshot


@admin.register(WebpageSnapshot)
class WebpageSnapshotAdmin(admin.ModelAdmin):

    date_hierarchy = 'captured_at'

    list_display = ['url', 'captured_at', 'get_admin_image']

    list_filter = ['captured_at']

    list_per_page = 10

    readonly_fields = ['url', 'captured_at', 'created_at', 'image']

    search_fields = ['url']

    def get_admin_image(self, obj):
        image = obj.get_image()
        thumbnail = obj.get_thumbnail('150x94')
        if hasattr(image, 'url'):
            return '<a href="{}"><img src="{}" alt="{}" /></a>'.format(
                image.url, thumbnail.url, obj)
        else:
            return '<img src="{}" alt="{}" />'.format(thumbnail.url, obj)
    get_admin_image.allow_tags = True
    get_admin_image.short_description = 'image'

    def get_readonly_fields(self, request, obj=None):
        if obj is None:
            return []
        else:
            return self.readonly_fields

    def save_model(self, request, obj, form, change):
        obj.get_image()
        return super(WebpageSnapshotAdmin, self).save_model(request, obj, form,
                                                            change)
