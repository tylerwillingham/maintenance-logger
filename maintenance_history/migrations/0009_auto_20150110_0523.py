# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance_history', '0008_auto_20150110_0437'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='maintenanceitem',
            options={'ordering': ['-date_entered']},
        ),
    ]
