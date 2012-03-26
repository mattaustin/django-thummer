# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from thummer.models import WebpageSnapshot


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
            return '<a href="%s"><img src="%s" alt="%s" /></a>' %(image.url,
                thumbnail.url, obj)
        else:
            return '<img src="%s" alt="%s" />' %(thumbnail.url, obj)
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

admin.site.register(WebpageSnapshot, WebpageSnapshotAdmin)

