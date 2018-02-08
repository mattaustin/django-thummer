# -*- coding: utf-8 -*-
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
