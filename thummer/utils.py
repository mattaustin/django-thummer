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


def get_thumbnail(url, geometry_string, **kwargs):
    """Finds or creates a valid ``WebpageSnapshot`` for the provided url,
    and returns its ``get_thumbnail`` method with the arguments provided."""
    from .models import WebpageSnapshot
    try:
        webpage_snapshot = WebpageSnapshot.objects.filter(
            url=url).valid().latest()
    except WebpageSnapshot.DoesNotExist:
        webpage_snapshot = WebpageSnapshot(url=url)
        webpage_snapshot.save()
    return webpage_snapshot.get_thumbnail(geometry_string, **kwargs)
