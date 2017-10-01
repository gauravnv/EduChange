# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-01 16:22
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=1000)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('upvotes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conditionName', models.CharField(choices=[('ASD', 'Autism Spectrum Disorders'), ('AD', 'Attachment Disorders'), ('ADHD', 'Attention Deficit/Hyperactivity Disorder'), ('A', 'Autism'), ('CD', 'Conduct Disorder'), ('DoWE', 'Disorder of Written Expression'), ('DMDD', 'Disruptive Mood Dysregulation Disorder'), ('Enc', 'Encopresis'), ('Enu', 'Enuresis'), ('ELD', 'Expressive Language Disorder'), ('MD', 'Mathematics Disorder'), ('ID', 'Intellectual Disability'), ('OCD', 'Obsessive-Compulsive Disorder'), ('ODD', 'Oppositional Defiant Disorder'), ('ReD', 'Reading Disorder'), ('RuD', 'Rumination Disorder'), ('SM', 'Selective Mutism'), ('SAD', 'Separation Anxiety Disorder'), ('SCD', 'Social Communication Disorder'), ('SMD', 'Stereotypic Movement Disorder'), ('S', 'Stuttering'), ('TD', "Tourette's Disorder"), ('TTD', 'Transient Tic Disorder')], max_length=10, verbose_name='Condition Name')),
                ('subCondition', models.CharField(max_length=50, verbose_name='Symptoms')),
                ('description', models.CharField(max_length=1000, verbose_name='Description')),
                ('writtenBy', models.CharField(max_length=1000, verbose_name='Source/Written by')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField(max_length=1000)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('upvotes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=75, verbose_name='First Name')),
                ('lastName', models.CharField(max_length=75, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('phoneNumber', models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+16045555555'.", regex='^\\+?1?\\d{10,12}$')], verbose_name='Number')),
                ('city', models.CharField(blank=True, max_length=30, null=True, verbose_name='City')),
                ('province', models.CharField(blank=True, choices=[('AB', 'Alberta'), ('BC', 'British Columbia'), ('ON', 'Ontario'), ('NS', 'Nova Scotia'), ('NL', 'Newfoundland and Labrador'), ('SK', 'Saskatchewan'), ('YT', 'Yukon'), ('MB', 'Manitoba'), ('NU', 'Nunavut'), ('PE', 'Prince Edward Island'), ('NT', 'Northwest Territories'), ('QC', 'Quebec'), ('NB', 'New Brunswick')], max_length=20, null=True, verbose_name='Province')),
                ('postalCode', models.CharField(blank=True, max_length=6, null=True, verbose_name='Postal Code')),
                ('numberOfUpvotes', models.IntegerField(blank=True, null=True, verbose_name='Number of Upvotes')),
                ('userSince', models.DateField(blank=True, default='', max_length=75, null=True, verbose_name='User Since')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('transcript', models.CharField(max_length=1000000, verbose_name='Transcript')),
                ('author', models.CharField(max_length=60, verbose_name='Author')),
                ('publication_date', models.DateField()),
                ('conditionName', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Hestia.Condition')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Hestia.User'),
        ),
        migrations.AddField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Hestia.User'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Hestia.Question'),
        ),
    ]
