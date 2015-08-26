# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('epedigree', '0009_lot_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='orderDate',
            field=models.DateField(default=datetime.datetime(2015, 8, 21, 21, 5, 45, 812928, tzinfo=utc), verbose_name=b'Order Date', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='title',
            field=models.CharField(max_length=80, verbose_name=b'Order No'),
        ),
    ]
