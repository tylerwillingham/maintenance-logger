# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance_history', '0006_maintenancereceipt'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenancereceipt',
            name='image',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='maintenancereceipt',
            name='note',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
