# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.http import HttpResponseRedirect
from thummer import get_thumbnail
import re

try:
    from django.views.generic import View
except ImportError:
    try:
        from cbv.generic import View
    except ImportError:
        raise ImportError('django-cbv is reqired for Django < 1.3')


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
            geometry_string = '%sx%s' %(geometry_string or '', height)
        return geometry_string
    
    def get_url(self):
        url = '%(scheme)s://%(hierarchical_part)s' %({
            'scheme': self.kwargs['scheme'],
            'hierarchical_part': self.kwargs['hierarchical_part']})
        return url
    
    def get_thumbnail(self):
        if self.get_crop():
            return get_thumbnail(self.get_url(), self.get_geometry_string())
        else:
            return get_thumbnail(self.get_url(), self.get_geometry_string(),
                crop='')

