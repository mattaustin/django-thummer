# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('thummer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpagesnapshot',
            name='image',
            field=sorl.thumbnail.fields.ImageField(unique=True, null=True, editable=False, upload_to='thummer/snapshots'),
        ),
        migrations.AlterUniqueTogether(
            name='webpagesnapshot',
            unique_together=set([('url', 'captured_at')]),
        ),
    ]
