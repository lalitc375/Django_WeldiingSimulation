# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webinterface', '0004_auto_20150606_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputdata',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='inputdata',
            name='underrelaxation_u_velocity',
            field=models.FloatField(default=0.6),
        ),
    ]
