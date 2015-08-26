# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0002_auto_20150812_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendence',
            name='attend_date',
            field=models.DateField(default=datetime.datetime(2015, 8, 12, 12, 30, 31, 221389, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
