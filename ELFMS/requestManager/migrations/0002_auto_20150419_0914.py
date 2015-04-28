# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('requestManager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resource',
            name='pub_year',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
