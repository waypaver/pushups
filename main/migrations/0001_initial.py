# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phoneNumber', models.CharField(default=b'', max_length=10)),
                ('emailAddress', models.CharField(default=b'', max_length=100)),
                ('firstName', models.CharField(default=b'', max_length=30)),
                ('lastName', models.CharField(default=b'', max_length=30)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateTimeStarted', models.DateTimeField()),
                ('score', models.IntegerField()),
                ('status', models.CharField(max_length=10)),
                ('participantID', models.ForeignKey(to='main.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
