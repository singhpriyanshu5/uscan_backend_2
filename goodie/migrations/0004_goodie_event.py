# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodie', '0003_auto_20150927_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodie',
            name='event',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
