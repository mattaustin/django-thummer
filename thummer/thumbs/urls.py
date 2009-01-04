#    thummer: website-snapshot/thumbnailing web service
#    Copyright (C) 2009  Matt Austin
#
#    This file is part of thummer.
#
#    thummer is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    thummer is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.conf.urls.defaults import *

from thummer.thumbs.models import Snapshot


#thumbs/
urlpatterns = patterns('',
    (r'^$', 'django.views.generic.list_detail.object_list', {'queryset': Snapshot.objects.all().order_by('-creation_date')[:10]}),
    (r'^(?P<width>\d+)/(?P<height>\d+)/(?P<crop>\d+)/(?P<url>https?://.*)\.png$', 'thummer.thumbs.views.thumb'),
    (r'^(?P<width>\d+)/(?P<height>\d+)/(?P<crop>\d+)/(?P<url>https?://.*)$', 'thummer.thumbs.views.thumb'),
)
