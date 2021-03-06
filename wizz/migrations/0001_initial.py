# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-23 08:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('counrty', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('iata_code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrivalStation', models.CharField(max_length=100)),
                ('arrivalStation_IATA', models.CharField(max_length=100)),
                ('departureStation', models.CharField(max_length=100)),
                ('departureStation_IATA', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('price', models.FloatField(blank=True, default=None, null=True)),
                ('price_USD', models.FloatField(blank=True, default=None, null=True)),
                ('currency', models.CharField(max_length=10)),
                ('air_company', models.CharField(max_length=10)),
                ('update_date', models.DateTimeField()),
                ('price_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='priceTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('templete_name', models.CharField(max_length=100)),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('date_from_return', models.DateField()),
                ('date_to_return', models.DateField()),
                ('arrivalStation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivalAirport', to='wizz.Airport')),
                ('arrivalStation_return', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivalAirport_return', to='wizz.Airport')),
                ('departureStation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departureAirport', to='wizz.Airport')),
                ('departureStation_return', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departureAirport_return', to='wizz.Airport')),
            ],
        ),
        migrations.CreateModel(
            name='priceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('priceType', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='pricetemplate',
            name='priceType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizz.priceType'),
        ),
    ]
