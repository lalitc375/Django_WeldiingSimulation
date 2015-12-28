# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webinterface', '0002_auto_20150602_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inputdata',
            name='dbUser',
        ),
        migrations.RemoveField(
            model_name='inputdata',
            name='id',
        ),
        migrations.AddField(
            model_name='inputdata',
            name='email',
            field=models.CharField(default='lalitc375@gmail.com', max_length=20, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
