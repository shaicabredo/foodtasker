# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-01 08:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0005_orderdetails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='diver',
            new_name='driver',
        ),
    ]
