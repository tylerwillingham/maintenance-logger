# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations


def update_seed_slugs(apps, schema_editor):
    slug_map = {
        'Normal':       'normal',
        'Preventative': 'preventative',
        'Modification': 'modification'
    }
    Type = apps.get_model('maintenance_history', 'MaintenanceType')

    for name, slug in slug_map.items():
        current_type = Type.objects.get(name=name)
        current_type.slug = slug
        current_type.save()


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance_history', '0003_maintenancetype_slug'),
    ]

    operations = [
        migrations.RunPython(update_seed_slugs)
    ]
