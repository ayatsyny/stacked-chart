# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-03 20:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload_data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datasession',
            old_name='session_id',
            new_name='session_key',
        ),
    ]