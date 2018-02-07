# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf import settings
from django.template import Library, Node, NodeList, TemplateSyntaxError
from django.utils.encoding import smart_str
from thummer.utils import get_thumbnail
import re


register = Library()
kw_pat = re.compile(r'^(?P<key>[\w]+)=(?P<value>.+)$')


class ThummerNodeBase(Node):
    """
    A Node that renders safely
    """
    nodelist_empty = NodeList()

    def render(self, context):
        try:
            return self._render(context)
        except Exception:
            if settings.DEBUG:
                raise
            # TODO: Log error
            return self.nodelist_empty.render(context)

    def _render(self, context):
        raise NotImplemented()


@register.tag('thummer')
class ThummerNode(ThummerNodeBase):
    child_nodelists = ('nodelist_url', 'nodelist_empty')
    error_msg = ('Syntax error. Expected: ``thummer url geometry '
                 '[key1=val1 key2=val2...] as var``')

    def __init__(self, parser, token):
        bits = token.split_contents()
        if len(bits) < 5 or bits[-2] != 'as':
            raise TemplateSyntaxError(self.error_msg)
        self.url = parser.compile_filter(bits[1])
        self.geometry = parser.compile_filter(bits[2])
        self.options = []
        for bit in bits[3:-2]:
            m = kw_pat.match(bit)
            if not m:
                raise TemplateSyntaxError(self.error_msg)
            key = smart_str(m.group('key'))
            expr = parser.compile_filter(m.group('value'))
            self.options.append((key, expr))
        self.as_var = bits[-1]
        self.nodelist_url = parser.parse(('empty', 'endthummer',))
        if parser.next_token().contents == 'empty':
            self.nodelist_empty = parser.parse(('endthummer',))
            parser.delete_first_token()

    def _render(self, context):
        url = self.url.resolve(context)
        geometry = self.geometry.resolve(context)
        options = {}
        for key, expr in self.options:
            noresolve = {'True': True, 'False': False, 'None': None}
            value = noresolve.get('{}'.format(expr), expr.resolve(context))
            if key == 'options':
                options.update(value)
            else:
                options[key] = value
        if url:
            thumbnail = get_thumbnail(url, geometry, **options)
        else:
            return self.nodelist_empty.render(context)
        context.push()
        context[self.as_var] = thumbnail
        output = self.nodelist_url.render(context)
        context.pop()
        return output

    def __iter__(self):
        for node in self.nodelist_url:
            yield node
        for node in self.nodelist_empty:
            yield node
