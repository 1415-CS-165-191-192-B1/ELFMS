# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requestManager', '0005_auto_20150505_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='approved',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resource',
            name='comment',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
    ]
