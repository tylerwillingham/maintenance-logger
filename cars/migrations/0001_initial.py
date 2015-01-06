# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('vin', models.CharField(max_length=100)),
                ('purchase_date', models.DateField()),
                ('sale_date', models.DateField()),
                ('year', models.CharField(max_length=4)),
                ('make', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('bodystyle', models.CharField(max_length=16)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
