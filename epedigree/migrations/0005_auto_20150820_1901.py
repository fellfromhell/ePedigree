# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epedigree', '0004_auto_20150816_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlines',
            name='lotnum',
            field=models.ForeignKey(related_name='olines', to='epedigree.Lot'),
        ),
    ]
