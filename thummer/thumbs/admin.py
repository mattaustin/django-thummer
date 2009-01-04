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

from django.contrib import admin
from thummer.thumbs.models import *

class SnapshotInline(admin.StackedInline):
  model = Snapshot
  extra = 0

class PageAdmin(admin.ModelAdmin):
  list_display = ('url', 'snapshots')
  inlines = [SnapshotInline]

admin.site.register(Page, PageAdmin)

class SnapshotAdmin(admin.ModelAdmin):
  fields = ['image']
  list_display = ('__unicode__', 'creation_date', 'image')
  list_filter = ['creation_date']
  search_fields = ['page__url']
  date_hierarchy = 'creation_date'

admin.site.register(Snapshot, SnapshotAdmin)
