# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def create_initial_maintenance_types(apps, schema_editor):
    initial_types = [
        'Normal',
        'Preventative',
        'Modification'
    ]
    Type = apps.get_model('maintenance_history', 'MaintenanceType')
    for type in initial_types:
        new_type = Type(name=type)
        new_type.save()


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance_history', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_maintenance_types)
    ]
