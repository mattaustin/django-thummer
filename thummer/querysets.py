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


from django.db import models
from django.utils import timezone

from . import settings


class WebpageSnapshotQuerySet(models.query.QuerySet):

    def valid(self):
        captured_after = timezone.now() - settings.VALID_FOR
        return self.filter(
            models.Q(captured_at__gte=captured_after) |
            models.Q(captured_at__isnull=True))

    def with_image(self):
        return self.filter(image__isnull=False)

    def without_image(self):
        return self.filter(image__isnull=True)
