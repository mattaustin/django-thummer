#!/usr/bin/env python
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

import codecs
from os import path

from distutils.core import Command
from setuptools import find_packages, setup

from thummer import __license__, __title__, __url__, __version__


BASE_DIR = path.dirname(path.abspath(__file__))


# Get the long description from the README file
with codecs.open(path.join(BASE_DIR, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


class DjangoCommand(Command):

    django_command_args = []

    django_settings = {
        'DATABASES': {'default': {'ENGINE': 'django.db.backends.sqlite3'}},
        'INSTALLED_APPS': ['thummer'],
        'MEDIA_ROOT': '/tmp/django-thummer/media/',
        'MIDDLEWARE_CLASSES': [],
        'ROOT_URLCONF': 'thummer.urls',
    }

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import django
        from django.conf import settings
        from django.core.management import call_command

        settings.configure(**self.django_settings)

        django.setup()
        return call_command(*self.django_command_args, verbosity=3)


class CheckCommand(DjangoCommand):

    django_command_args = ['check']


class MakeMigrationsCommand(DjangoCommand):

    django_command_args = ['makemigrations', 'thummer']


class TestCommand(DjangoCommand):

    django_command_args = ['test', 'thummer.tests']


setup(

    name=__title__,

    version=__version__,

    description='A website screenshot and thumbnailing app for Django.',
    long_description=long_description,

    url=__url__,

    author='Matt Austin',
    author_email='devops@mattaustin.com.au',

    license=__license__,

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Multimedia :: Graphics :: Capture',
    ],

    keywords='thummer django website snapshot screenshot thumbnail',

    packages=find_packages(),

    cmdclass={
        'djangocheck': CheckCommand,
        'makemigrations': MakeMigrationsCommand,
        'test': TestCommand
    },

    install_requires=[
        'django>=1.8,!=1.9.*,!=1.10.*,<=2.1',
        'pillow~=5.0',
        'python-dateutil~=2.6',
        'selenium~=3.9',
        'sorl-thumbnail~=12.4',
    ],

    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',

    extras_require={
        'tests': [
            'coverage~=4.5',
            'freezegun~=0.3',
            'mock~=2.0',
            'pytz',
        ],
    },

)
