# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0027_auto_20171209_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enseignelumineuse',
            name='longueur',
            field=models.CharField(choices=[('2m', '2m'), ('3m', '3m'), ('5m', '5m'), ('10', '10m'), ('1,20m', '1,20m'), ('15m', '15m'), ('20m', '20m'), ('25m', '25m'), ('50m', '50m'), ('100m', '100m')], max_length=20),
        ),
        migrations.AlterField(
            model_name='rallonge',
            name='longueur',
            field=models.CharField(choices=[('2m', '2m'), ('3m', '3m'), ('5m', '5m'), ('10', '10m'), ('1,20m', '1,20m'), ('15m', '15m'), ('20m', '20m'), ('25m', '25m'), ('50m', '50m'), ('100m', '100m')], max_length=20),
        ),
    ]
