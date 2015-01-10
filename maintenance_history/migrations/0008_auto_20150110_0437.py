# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance_history', '0007_auto_20150110_0413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenanceitem',
            name='vehicle',
            field=models.ForeignKey(to='cars.Vehicle', related_name='maintenance'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='maintenancereceipt',
            name='maintenance_item',
            field=models.ForeignKey(to='maintenance_history.MaintenanceItem', related_name='receipt'),
            preserve_default=True,
        ),
    ]
