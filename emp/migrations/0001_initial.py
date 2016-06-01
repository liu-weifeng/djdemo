# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 12:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
            ],
            options={
                'db_table': 'application',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp.Department')),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.AddField(
            model_name='application',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp.Article'),
        ),
        migrations.AddField(
            model_name='application',
            name='emp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp.Employee'),
        ),
    ]
