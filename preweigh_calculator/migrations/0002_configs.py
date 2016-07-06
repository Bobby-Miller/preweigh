# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preweigh_calculator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variable', models.CharField(max_length=32)),
                ('int_val', models.IntegerField(null=True)),
                ('float_val', models.FloatField(null=True)),
                ('str_val', models.CharField(max_length=255, blank=True)),
                ('bool_val', models.NullBooleanField()),
            ],
        ),
    ]
