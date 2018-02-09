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


__title__ = 'django-thummer'

__version__ = '3.0.dev1'

__url__ = 'https://github.com/mattaustin/django-thummer'

__author__ = 'Matt Austin <devops@mattaustin.com.au>'

__copyright__ = 'Copyright 2011-2018 Matt Austin'

__license__ = 'Apache 2.0'


default_app_config = 'thummer.apps.AppConfig'


def get_thumbnail(*args, **kwargs):
    from .utils import get_thumbnail
    return get_thumbnail(*args, **kwargs)
