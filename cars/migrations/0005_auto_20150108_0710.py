# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20150106_0601'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Car',
            new_name='Vehicle',
        ),
    ]
