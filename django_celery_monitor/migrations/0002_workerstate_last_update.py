# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celery_monitor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workerstate',
            name='last_update',
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                auto_now=True,
                verbose_name='last update',
            ),
            preserve_default=False,
        ),
    ]
