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

from datetime import datetime

import pytz
from django.core.exceptions import ValidationError
from django.test import TestCase

from thummer.models import WebpageSnapshot


try:
    from unittest.mock import patch
except ImportError:
    from mock import patch


UTC = pytz.timezone('Etc/UTC')


class TestWebpageSnapshot(TestCase):

    def setUp(self):
        self.url = 'https://github.com/mattaustin/django-thummer/'

    def test__generate_image_filename_raises_validation_error_if_captured_at_is_none(self):  # noqa: E501
        obj = WebpageSnapshot(url=self.url)

        with self.assertRaises(ValidationError):
            obj._generate_image_filename()

    def test__generate_image_filename_returns_string_ending_with_png(self):
        obj = WebpageSnapshot(url=self.url,
                              captured_at=UTC.localize(datetime(2018, 1, 1)))

        result = obj._generate_image_filename()

        self.assertTrue(result.endswith('.png'))

    def test__generate_image_filename_returns_string_starting_with_upload_path(self):  # noqa: E501
        upload_prefix = 'upload/prefix'
        obj = WebpageSnapshot(url=self.url,
                              captured_at=UTC.localize(datetime(2018, 1, 1)))

        with patch('thummer.settings.UPLOAD_PATH', upload_prefix):
            result = obj._generate_image_filename()

        self.assertTrue(result.startswith(upload_prefix))

    @patch('thummer.settings.UPLOAD_PATH', 'thummer/test')
    def test__generate_image_filename_returns_expected_filename(self):
        expected_filename = 'thummer/test/a117ee7b996760879baceb506966e6ec.png'
        timestamp = UTC.localize(datetime(2018, 1, 1))

        obj = WebpageSnapshot(url=self.url, captured_at=timestamp)
        result = obj._generate_image_filename()

        self.assertEqual(expected_filename, result)
