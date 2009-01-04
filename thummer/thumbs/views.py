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

from django.http import HttpResponse, HttpResponseNotModified, HttpResponseRedirect
from django.core.files import File
from django.views.decorators.cache import cache_page

from thummer.thumbs.models import *

# Tells user agents to cache the response for a year
@cache_page(60 * 60 * 24 * 7 * 52)

def thumb(request, url, width, height, crop):
  
  # Determine if Page exists
  if Page.objects.filter(url=url):
    p = Page.objects.get(url=url)
  else:
    # Create new page
    p = Page(url=url)
    p.save()
  
  # Determine if Shapshot exists
  if p.snapshot_set.all():
    # Then get the latest snapshot
    s = p.snapshot_set.latest()
  else:
    # Capture the page
    s = p.capture()
  
  # Serve the thumbnail
  t = s.thumbnail(width, height, bool(int(crop)))
  
  if not settings.REDIRECT_THUMBS:
    # This will serve the image using django.
    return HttpResponse(open(t.dest, 'rb').read(), mimetype='image/png')
  else:
    # This will send a HTTP 302 temporary redirect response, so that the image is served via the appropriate server for static media.
    return HttpResponseRedirect(t.absolute_url)

