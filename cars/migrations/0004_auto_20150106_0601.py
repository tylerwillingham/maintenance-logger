# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20150106_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='purchase_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='car',
            name='sale_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
