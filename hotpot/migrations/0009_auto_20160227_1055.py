# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotpot', '0008_auto_20160227_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itembatch',
            name='amount',
            field=models.PositiveIntegerField(),
        ),
    ]
