# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-20 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chenjianzhong', '0005_experience_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='company',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]