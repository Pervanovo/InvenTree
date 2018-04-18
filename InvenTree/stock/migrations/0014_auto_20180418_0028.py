# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-17 14:28
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0013_auto_20180417_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockitem',
            name='status',
            field=models.PositiveIntegerField(choices=[(10, 'OK'), (50, 'Attention needed'), (55, 'Damaged'), (60, 'Destroyed')], default=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]