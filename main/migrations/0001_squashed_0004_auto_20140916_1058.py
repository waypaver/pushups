# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [('main', '0001_squashed_0010_delete_schedule'), ('main', '0003_auto_20140916_1055'), ('main', '0004_auto_20140916_1058')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('dateTimeStarted', models.DateTimeField(auto_now_add=True)),
                ('score', models.IntegerField(default=0)),
                ('status', models.CharField(default='pending', max_length=10)),
                ('participantID', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
