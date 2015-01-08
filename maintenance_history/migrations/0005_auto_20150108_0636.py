# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance_history', '0004_auto_20150108_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenancetype',
            name='slug',
            field=models.SlugField(max_length=20, unique=True, default='slug'),
            preserve_default=True,
        ),
    ]
