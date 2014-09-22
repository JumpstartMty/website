# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jumpstarters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jumpstarter',
            name='profileImg',
            field=models.ImageField(upload_to='photos', blank=True, null=True),
            preserve_default=True,
        ),
    ]
