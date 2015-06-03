# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requestManager', '0006_auto_20150505_2133'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='resource',
            unique_together=set([]),
        ),
    ]
