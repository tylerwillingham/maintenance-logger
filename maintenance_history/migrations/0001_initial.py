# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_auto_20150108_0710'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaintenanceItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('summary', models.TextField()),
                ('performed_date', models.DateField()),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
                ('date_last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MaintenanceType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='maintenanceitem',
            name='type',
            field=models.ForeignKey(to='maintenance_history.MaintenanceType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='maintenanceitem',
            name='vehicle',
            field=models.ForeignKey(to='cars.Vehicle'),
            preserve_default=True,
        ),
    ]
