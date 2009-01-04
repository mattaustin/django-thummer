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

import Image
import md5
import subprocess
import datetime

from django.db import models
from django.conf import settings

from sorl.thumbnail.fields import ImageWithThumbnailsField
from sorl.thumbnail.main import DjangoThumbnail


class Page(models.Model):
  url = models.URLField(verify_exists=True,unique=True)
  def __unicode__(self):
    return self.url
  
  def capture(self):
    snapshotfilename = md5.new(str(datetime.datetime.now())+self.url).hexdigest() + '.png'
    try:
      # Code needs cleaning up!
      if not settings.XVFB:
      	# For machines already with an X server (desktops)
      	if settings.USE_GNOMEWEBPHOTO:
      	  # Use gnome-web-photo.
      	  subprocess.check_call(['gnome-web-photo', self.url, settings.MEDIA_ROOT + '/snapshots/' + snapshotfilename])
      	else:
      	  # Use cutycapt.
      	  subprocess.check_call([settings.CUTYCAPT, '--url=' + self.url, '--out=' + settings.MEDIA_ROOT + '/snapshots/' + snapshotfilename])
      else:
      	# For servers - uses the XVFB virtual X server environment (apt-get install xvfb)
      	if settings.USE_GNOMEWEBPHOTO:
      	  # Use gnome-web-photo.
      	  subprocess.check_call(['xvfb-run', '--auto-servernum', '--server-args=-screen 0, 1024x768x24', 'gnome-web-photo', self.url, settings.MEDIA_ROOT + '/snapshots/' + snapshotfilename])
      	else:
      	  # Use cutycapt.
      	  subprocess.check_call(['xvfb-run', '--auto-servernum', '--server-args=-screen 0, 1024x768x24', settings.CUTYCAPT, '--url=' + self.url, '--out=' + settings.MEDIA_ROOT + '/snapshots/' + snapshotfilename])
      s = Snapshot(page=self,image='snapshots/' + snapshotfilename)
      s.save()
    except subprocess.CalledProcessError:
      s = Snapshot(page=self,image='placeholder.png')
    return s
  
  def snapshots(self):
    return int(self.snapshot_set.count())


class Snapshot(models.Model):
  page = models.ForeignKey(Page)
  image = ImageWithThumbnailsField(upload_to='snapshots')
  creation_date = models.DateTimeField(auto_now_add=True)
  def __unicode__(self):
    return self.page.url

  def thumbnail(self, width=None, height=None, autocrop=False):
    if width is None or int(width) > int(self.image.width) or int(width) < 1:
      width = self.image.width
    if height is None or int(height) > int(self.image.height) or int(height) < 1:
      height = self.image.height
    if autocrop:
      t = DjangoThumbnail(self.image, (int(width), int(height)), ['crop'])
    else:
      t = DjangoThumbnail(self.image, (int(width), int(height)))
    return t

  class Meta:
    get_latest_by = "creation_date"
    ordering = ['-creation_date']
