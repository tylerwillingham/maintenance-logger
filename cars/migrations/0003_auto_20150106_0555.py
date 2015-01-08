# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20150106_0554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='vin',
            field=models.CharField(blank=True, max_length=100),
            preserve_default=True,
        ),
    ]
