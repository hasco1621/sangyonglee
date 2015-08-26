# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0003_attendence_attend_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendence',
            options={'ordering': ['-created_at', 'id']},
        ),
    ]
