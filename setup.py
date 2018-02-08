#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import codecs
from os import path

from distutils.core import Command
from setuptools import find_packages, setup

from thummer import __title__, __url__, __version__


BASE_DIR = path.dirname(path.abspath(__file__))


# Get the long description from the README file
with codecs.open(path.join(BASE_DIR, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


class TestCommand(Command):

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import django
        from django.conf import settings
        from django.core.management import call_command

        settings.configure(
            DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3'}},
            INSTALLED_APPS=['thummer'],
            MIDDLEWARE_CLASSES=[],
            TEMPLATES=[{
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'APP_DIRS': True}],
            MEDIA_ROOT='/tmp/django-thummer/media/',
        )

        django.setup()
        call_command('test', 'thummer.tests', verbosity=3)


setup(

    name=__title__,

    version=__version__,

    description='A website screenshot and thumbnailing app for Django.',
    long_description=long_description,

    url=__url__,

    author='Matt Austin',
    author_email='devops@mattaustin.com.au',

    license='Apache',

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

    cmdclass={'test': TestCommand},

    install_requires=[
        'django>=1.8,!=1.9.*,!=1.10.*,<=2.1',
        'pillow~=5.0',
        'python-dateutil~=2.6',
        'selenium~=3.9',
        'sorl-thumbnail~=12.4',
    ],

    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',

    extras_require={
        'tests': ['freezegun==0.3.9'],
    },

)
