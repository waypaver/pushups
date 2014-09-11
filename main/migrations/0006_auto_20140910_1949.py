# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20140910_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='day',
            field=models.IntegerField(max_length=10, choices=[(0, b'Monday'), (1, b'Tuesday'), (2, b'Wednesday'), (3, b'Thursday'), (4, b'Friday'), (5, b'Saturday'), (6, b'Sunday')]),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='dayPart',
            field=models.IntegerField(max_length=2, choices=[(0, b'AM'), (1, b'PM')]),
        ),
    ]
