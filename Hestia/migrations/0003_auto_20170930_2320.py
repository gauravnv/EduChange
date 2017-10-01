# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 06:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hestia', '0002_auto_20170930_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField(max_length=1000)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('upvotes', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='parent',
            name='province',
            field=models.CharField(blank=True, choices=[('NL', 'Newfoundland and Labrador'), ('AB', 'Alberta'), ('YT', 'Yukon'), ('ON', 'Ontario'), ('NU', 'Nunavut'), ('BC', 'British Columbia'), ('QC', 'Quebec'), ('PE', 'Prince Edward Island'), ('NT', 'Northwest Territories'), ('NB', 'New Brunswick'), ('SK', 'Saskatchewan'), ('MB', 'Manitoba'), ('NS', 'Nova Scotia')], max_length=20, null=True, verbose_name='Province'),
        ),
    ]
