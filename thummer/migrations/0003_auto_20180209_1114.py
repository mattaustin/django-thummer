# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thummer', '0002_auto_20180208_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpagesnapshot',
            name='capture_width',
            field=models.IntegerField(default=1024, editable=False),
        ),
    ]
