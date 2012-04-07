========
Settings
========


``THUMMER_PLACEHOLDER_DEFAULTS``
--------------------------------

Default: ``{'crop': 'center', 'upscale': False, 'format': 'PNG'}`` (Dictionary)

A keywords dictionary passed to ``sorl.thumbnail`` when generating placeholder 
thumbnails.


``THUMMER_PLACEHOLDER_PATH``
----------------------------

Default: ``'thummer/placeholder.png'`` (String)

The path to the placeholder image in your ``staticfiles`` storage.


``THUMMER_QUEUE_SNAPSHOTS``
---------------------------

Default: ``True`` (Boolean) if ``'djcelery'`` is in Django's 
``'INSTALLED_APPS'`` setting.

Determine if thumbnail generation should be queued for background processing 
using ``django-celery`` (recommended).


``THUMMER_SNAPSHOTS_VALID_FOR``
-------------------------------

Default: ``dateutil.relativedelta.relativedelta(months=+3)`` (A dateutil 
relativedelta of 3 months)

The period of time that a thumbnail snapshot of a url is valid for, before a 
new thumbnail is generated.


``THUMMER_STORAGE``
-------------------

Default: ``django.core.files.storage.default_storage`` (Django's configured 
default storage)

Storage instance to use for thumbnail media.


``THUMMER_THUMBNAIL_DEFAULTS``
------------------------------

Default: ``{'crop': 'left top', 'upscale': False, 'format': 'JPEG'}`` 
(Dictionary)

A keywords dictionary passed to ``sorl.thumbnail`` when generating thumbnails.


``THUMMER_UPLOAD_PATH``
-----------------------

Default: ``'thummer/snapshots'`` (String)

The path prefix to store thumbnails under in ``THUMMER_STORAGE``.

