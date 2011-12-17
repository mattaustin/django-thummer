# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from setuptools import setup, find_packages
from thummer.meta import VERSION


setup(name='django-thummer',
    author='Matt Austin', author_email='mail@mattaustin.me.uk',
    url='https://github.com/MattAustin/django-thummer',
    version=unicode(VERSION),
    packages=find_packages(),
    include_package_data=True,
    install_requires=['django', 'python-dateutil==2.0',
        'pyvirtualdisplay==0.0.7', 'selenium==2.15.0',
        'sorl-thumbnail==11.09.1'],
    )

