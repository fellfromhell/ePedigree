# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('clientID', models.AutoField(serialize=False, verbose_name=b'Client', primary_key=True, db_column=b'clientID')),
                ('cName', models.CharField(max_length=80, verbose_name=b'Client Name')),
                ('cAddressLine1', models.CharField(max_length=60, null=True, verbose_name=b'Street Address', blank=True)),
                ('cAddressLine2', models.CharField(max_length=60, null=True, verbose_name=b'Street Address 2', blank=True)),
                ('cCity', models.CharField(max_length=30, null=True, verbose_name=b'City', blank=True)),
                ('cState', models.CharField(max_length=30, null=True, verbose_name=b'State', blank=True)),
                ('cPostalCode', models.CharField(max_length=15, null=True, verbose_name=b'Zip', blank=True)),
                ('sName', models.CharField(max_length=80, null=True, verbose_name=b'Client Ship Name', blank=True)),
                ('sAddressLine1', models.CharField(max_length=60, null=True, verbose_name=b'Street Address', blank=True)),
                ('sAddressLine2', models.CharField(max_length=60, null=True, verbose_name=b'Street Address 2', blank=True)),
                ('sCity', models.CharField(max_length=30, null=True, verbose_name=b'City', blank=True)),
                ('sState', models.CharField(max_length=30, null=True, verbose_name=b'State', blank=True)),
                ('sPostalCode', models.CharField(max_length=15, null=True, verbose_name=b'Zip', blank=True)),
            ],
            options={
                'ordering': ['-clientID'],
            },
        ),
        migrations.CreateModel(
            name='Following',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clientID', models.ForeignKey(to='epedigree.Client', db_column=b'clientID')),
            ],
            options={
                'ordering': ['-user_id'],
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=4, decimal_places=2)),
                ('measurement', models.SmallIntegerField(choices=[(1, b'piece'), (2, b'liter'), (3, b'cup'), (4, b'tablespoon'), (5, b'teaspoon')])),
                ('food', models.ForeignKey(to='epedigree.Food')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=170)),
            ],
        ),
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lotNumber', models.CharField(max_length=80)),
                ('expiryDate', models.DateField(verbose_name=b'Expiration Date', blank=True)),
                ('ndc', models.CharField(max_length=30, blank=True)),
                ('description', models.TextField(blank=True)),
                ('status', models.SmallIntegerField(choices=[(1, b'Active'), (2, b'Hold'), (3, b'Quarantined'), (4, b'Returned'), (5, b'Recalled'), (6, b'Expired')])),
                ('item', models.ForeignKey(related_name='items', to='epedigree.Item')),
            ],
        ),
        migrations.CreateModel(
            name='LotTransactions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orderList', models.IntegerField()),
                ('soldToName', models.CharField(max_length=80)),
                ('soldToAddressLine1', models.CharField(max_length=60)),
                ('soldToAddressLine2', models.CharField(max_length=60, blank=True)),
                ('soldToCity', models.CharField(max_length=30, blank=True)),
                ('soldToState', models.CharField(max_length=30, blank=True)),
                ('soldToPostalCode', models.CharField(max_length=15, blank=True)),
                ('shipToName', models.CharField(max_length=80, blank=True)),
                ('shipToAddressLine1', models.CharField(max_length=60, blank=True)),
                ('shipToAddressLine2', models.CharField(max_length=60, blank=True)),
                ('shipToCity', models.CharField(max_length=30, blank=True)),
                ('shipToState', models.CharField(max_length=30, blank=True)),
                ('shipToPostalCode', models.CharField(max_length=15, blank=True)),
                ('lot', models.ForeignKey(related_name='lots', to='epedigree.Lot')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField(blank=True)),
                ('clientID', models.ForeignKey(related_name='corders', verbose_name=b'Client', to='epedigree.Client')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLines',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=4, decimal_places=2)),
                ('measurement', models.SmallIntegerField(choices=[(1, b'piece'), (2, b'liter'), (3, b'cup'), (4, b'tablespoon'), (5, b'teaspoon')])),
                ('item', models.ForeignKey(related_name='oitems', to='epedigree.Item')),
                ('lotnum', models.ForeignKey(to='epedigree.Lot')),
                ('order', models.ForeignKey(related_name='orders', to='epedigree.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80)),
                ('slug', models.SlugField(unique=True, max_length=80)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(related_name='profiles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(to='epedigree.Recipe'),
        ),
        migrations.AddField(
            model_name='following',
            name='user_id',
            field=models.ForeignKey(related_name='follows', to='epedigree.UserProfile'),
        ),
    ]
