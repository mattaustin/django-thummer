# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db.models import Manager


class QuerySetManager(Manager):

    # http://djangosnippets.org/snippets/734/
    def __getattr__(self, attr, *args):
        return getattr(self.get_query_set(), attr, *args)

    def get_query_set(self):
        return self.model.QuerySet(self.model)
