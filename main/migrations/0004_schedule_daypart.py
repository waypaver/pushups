# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='dayPart',
            field=models.CharField(default=0, max_length=2, choices=[(0, b'AM'), (1, b'PM')]),
            preserve_default=False,
        ),
    ]
