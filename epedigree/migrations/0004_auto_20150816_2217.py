# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epedigree', '0003_auto_20150814_0310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='food',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='recipe',
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['cName']},
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.SmallIntegerField(default=7, choices=[(1, b'archived'), (2, b'cancelled'), (3, b'converted'), (4, b'declined'), (5, b'draft'), (6, b'expired'), (7, b'open'), (8, b'overdue'), (9, b'paid'), (10, b'partial'), (11, b'revised'), (12, b'sent'), (13, b'unopen')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='Food',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.DeleteModel(
            name='Recipe',
        ),
    ]
