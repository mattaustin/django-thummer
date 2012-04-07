=====
Setup
=====

Requirements
------------
django-thummer requires Firefox and Xvfb. On Debian/Ubuntu systems these can be 
installed using::

    sudo apt-get install firefox xvfb


Installation
------------
django-thummer can be installed to your Python environment using pip::

    pip install django-thummer

Then add ``thummer`` to ``INSTALLED_APPS`` in your Django settings file, and 
sync the database. If you're using `South <http://south.aeracode.org/>`_, then 
migrations are provided.

Using Celery for background thumbnail capture
=============================================
It is highly recommended to use Celery for background thumbnail capture.
By default, django-thummer will automatically use Celery if it is available.
Both celery and django-celery can be installed to your Python environment using 
pip::

    pip install django-celery

Configuring celery can be tricky, and you should carefully read both the 
`django-celery documentation <http://pypi.python.org/pypi/django-celery>`_ 
and `celery documentation <http://docs.celeryproject.org/>`_.

