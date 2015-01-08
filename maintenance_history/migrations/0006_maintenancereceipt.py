# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance_history', '0005_auto_20150108_0636'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaintenanceReceipt',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('note', models.TextField()),
                ('maintenance_item', models.ForeignKey(to='maintenance_history.MaintenanceItem')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
