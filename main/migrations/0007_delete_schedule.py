# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20140910_1949'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]
