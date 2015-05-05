# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requestManager', '0003_auto_20150428_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='price',
            field=models.DecimalField(null=True, verbose_name=b'Price', max_digits=8, decimal_places=2),
            preserve_default=True,
        ),
    ]
