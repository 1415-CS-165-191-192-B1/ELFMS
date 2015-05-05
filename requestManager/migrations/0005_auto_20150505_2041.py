# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requestManager', '0004_resource_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='tag',
        ),
        migrations.AlterField(
            model_name='resource',
            name='comment',
            field=models.CharField(default=b'', max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resource',
            name='subscription_type',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
