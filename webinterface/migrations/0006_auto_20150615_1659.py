# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webinterface', '0005_auto_20150606_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputdata',
            name='x_location_tool',
            field=models.FloatField(default=8.5),
        ),
        migrations.AlterField(
            model_name='inputdata',
            name='y_location_tool',
            field=models.FloatField(default=8.5),
        ),
    ]
