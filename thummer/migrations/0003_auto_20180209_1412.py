# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from thummer import settings


class Migration(migrations.Migration):

    dependencies = [
        ('thummer', '0002_auto_20180208_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpagesnapshot',
            name='capture_width',
            field=models.IntegerField(
                default=getattr(settings, 'DEFAULT_CAPTURE_WIDTH', 1280),
                editable=False),
        ),
        migrations.AlterUniqueTogether(
            name='webpagesnapshot',
            unique_together=set([('url', 'capture_width', 'captured_at')]),
        ),
    ]
