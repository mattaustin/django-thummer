=====
Setup
=====


Requirements
------------

django-thummer requires Firefox. On Debian/Ubuntu systems this can be installed
using::

    sudo apt-get install firefox


``geckodriver`` is also required. This can be downloaded from the
`geckodriver releases page <https://github.com/mozilla/geckodriver/releases>`_,
and extracted to somewhere on the system path, e.g. ``/usr/local/bin``.


Installation
------------

django-thummer can be installed to your Python environment using pip::

    python -m pip install django-thummer

Then add ``thummer`` to ``INSTALLED_APPS`` in your Django settings file.


Using Celery for background thumbnail capture
=============================================

It is highly recommended to use Celery for background thumbnail capture.
By default, django-thummer will automatically use Celery if it is available.

Configuring celery can be tricky, and you should carefully the
`celery documentation <http://docs.celeryproject.org/en/latest/django/index.html>`_.
