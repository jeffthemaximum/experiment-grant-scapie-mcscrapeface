# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-15 18:52
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(max_length=500)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
