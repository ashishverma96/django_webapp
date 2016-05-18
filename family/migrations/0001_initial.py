# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-19 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sirname', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('dateofbirth', models.CharField(max_length=100)),
                ('Address', models.CharField(blank=True, max_length=100)),
                ('bloodgroup', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=10)),
                ('image', models.ImageField(blank=True, upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='userVerificationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('code', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
