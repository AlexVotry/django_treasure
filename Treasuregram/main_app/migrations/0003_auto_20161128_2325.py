# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 23:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20161128_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treasure',
            name='image',
            field=models.ImageField(default='media/treasure_images/racerX.jpg', upload_to='treasure_images'),
        ),
    ]
