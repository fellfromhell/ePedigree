# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epedigree', '0006_auto_20150820_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlines',
            name='amount',
            field=models.DecimalField(max_digits=6, decimal_places=0),
        ),
    ]
