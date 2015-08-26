# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epedigree', '0007_auto_20150820_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lottransactions',
            name='orderList',
        ),
    ]
