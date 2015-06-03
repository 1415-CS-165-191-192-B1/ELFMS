# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requestManager', '0002_auto_20150419_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='author',
            field=models.CharField(max_length=50, verbose_name=b'Author'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resource',
            name='comment',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resource',
            name='edition',
            field=models.CharField(max_length=50, verbose_name=b'Edition'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resource',
            name='title',
            field=models.CharField(max_length=50, verbose_name=b'Title'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='resource',
            unique_together=set([('title', 'edition')]),
        ),
    ]
