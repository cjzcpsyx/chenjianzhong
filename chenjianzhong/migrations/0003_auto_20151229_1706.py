# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chenjianzhong', '0002_auto_20151229_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='added',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 29, 17, 6, 0, 751842, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='experience',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 29, 17, 6, 3, 376768, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='added',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 29, 17, 6, 5, 871920, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 29, 17, 6, 7, 672135, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
