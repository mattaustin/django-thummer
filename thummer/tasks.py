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


try:
    from celery import shared_task
except ImportError:
    from functools import wraps

    # Faux shared_task decorator
    def shared_task(*args, **kwargs):
        def factory(func):
            @wraps(func)
            def decorator(*args, **kwargs):
                return func(*args, **kwargs)
            return decorator
        return factory


@shared_task(ignore_result=True)
def capture(pk):
    from .models import WebpageSnapshot
    instance = WebpageSnapshot.objects.get(pk=pk)
    return instance._capture()
