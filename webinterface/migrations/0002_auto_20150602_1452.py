# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webinterface', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dbuser',
            name='id',
        ),
        migrations.AlterField(
            model_name='dbuser',
            name='email',
            field=models.CharField(max_length=20, serialize=False, primary_key=True),
        ),
    ]
