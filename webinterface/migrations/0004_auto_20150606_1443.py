# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webinterface', '0003_auto_20150606_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='inputdata',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=0, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inputdata',
            name='email',
            field=models.CharField(max_length=20),
        ),
    ]
