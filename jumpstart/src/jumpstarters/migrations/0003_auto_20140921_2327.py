# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jumpstarters', '0002_jumpstarter_profileimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jumpstarter',
            name='description',
            field=models.TextField(null=True, max_length=200, blank=True),
        ),
    ]
