# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preweigh_calculator', '0002_configs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('task', models.CharField(max_length=127)),
                ('minutes', models.FloatField()),
                ('people', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='configs',
            options={'verbose_name_plural': 'configs'},
        ),
        migrations.AlterField(
            model_name='configs',
            name='float_val',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='configs',
            name='int_val',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
