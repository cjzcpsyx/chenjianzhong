# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chenjianzhong', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='description',
            field=models.TextField(default='placeholder'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(default='placeholder'),
            preserve_default=False,
        ),
    ]
