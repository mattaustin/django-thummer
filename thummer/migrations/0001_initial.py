# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebpageSnapshot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(db_index=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='thummer/snapshots', null=True, editable=False)),
                ('capture_width', models.IntegerField(default=1680, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('captured_at', models.DateTimeField(null=True, editable=False)),
            ],
            options={
                'ordering': ['-captured_at'],
                'get_latest_by': 'captured_at',
            },
        ),
    ]
