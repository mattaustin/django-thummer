# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thummer', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='webpagesnapshot',
            unique_together=set([('image',), ('url', 'captured_at')]),
        ),
    ]
