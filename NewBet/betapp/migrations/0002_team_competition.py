# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 08:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('betapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='competition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='betapp.Competition'),
        ),
    ]