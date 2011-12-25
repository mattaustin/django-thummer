=====
Setup
=====

Requirements
------------
django-thummer requires Firefox and Xvfb. On Debian/Ubuntu systems these can be installed using::

    sudo apt-get install firefox xvfb


Installation
------------
django-thummer can be installed to your Python environment using pip::

    pip install django-thummer

Then add ``thummer`` to ``INSTALLED_APPS`` in your Django settings file, and sync the database. If you're using `South <http://south.aeracode.org/>`_, then migrations are provided.

