# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='dateTimeStarted',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='workout',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='workout',
            name='status',
            field=models.CharField(default=b'pending', max_length=10),
        ),
    ]
