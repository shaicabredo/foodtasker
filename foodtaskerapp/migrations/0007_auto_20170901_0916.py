# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-01 09:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0006_auto_20170901_0856'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetails',
            old_name='sub_tital',
            new_name='sub_total',
        ),
    ]
