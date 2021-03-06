# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 15:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, default='Processing image... Refresh to check for results.', max_length=120, null=True)),
                ('number_1', models.IntegerField()),
                ('number_2', models.IntegerField()),
                ('total', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paragon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('image_data', models.TextField(blank=True, default='Processing image... Refresh to check for results. If that doesnt help please wait or do something else one the website', null=True)),
                ('user1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ParagonItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cena', models.CharField(blank=True, max_length=120, null=True)),
                ('produkt', models.CharField(blank=True, max_length=120, null=True)),
                ('id_paragonu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='receipt.Paragon')),
            ],
        ),
    ]
