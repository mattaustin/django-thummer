==============
django-thummer
==============
A website snapshot and thumbnailing app for django. Uses firefox, selenium, and
sorl-thumbnail.


Getting started
===============

Requirements
------------
django-thummer requires Firefox and Xvfb. On Debian/Ubuntu systems these can be installed using::

    sudo apt-get install firefox xvfb


Installation
------------
django-thummer can be installed to your Python environment using pip::

    pip install django-thummer

Then add ``thummer`` to ``INSTALLED_APPS`` in your Django settings file, and sync the database. If you're using `South <http://south.aeracode.org/>`_, then migrations are provided.


Basic usage
-----------
::

    from thummer.utils import get_thumbnail
    
    thumbnail = get_thumbnail('http://www.example.com/', '400x400')


Credits
=======
Special thanks to the `sorl-thumbnail <https://github.com/sorl/sorl-thumbnail>`_ and `selenium <http://code.google.com/p/selenium/>`_ projects. Thanks also to the blog posts which originally got me thinking about the project:

* http://coreygoldberg.blogspot.com/2011/06/python-headless-selenium-webdriver.html
* http://lapin-blanc.net/09/11/2008/django-website-thumbnail-generator/


To-do
=====
* Snapshot error handling
* Documentation
* Template tag
* Celery tasks
* Placeholder image
* Management commands
* Tests
* Logging
* Cache redirect response?

