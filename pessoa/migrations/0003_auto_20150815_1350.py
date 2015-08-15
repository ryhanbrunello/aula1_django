# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0002_auto_20150815_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='nome',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
