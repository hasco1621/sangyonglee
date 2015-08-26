# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendence',
            old_name='creat_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='attendence',
            old_name='st_name',
            new_name='student_name',
        ),
        migrations.AddField(
            model_name='attendence',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 8, 12, 11, 23, 49, 862524, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
