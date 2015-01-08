# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance_history', '0002_auto_20150108_0321'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenancetype',
            name='slug',
            field=models.SlugField(default='slug', max_length=20),
            preserve_default=True,
        ),
    ]
