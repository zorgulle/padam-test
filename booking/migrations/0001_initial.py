# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-12 14:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_number', models.CharField(max_length=5, verbose_name='N')),
                ('route', models.CharField(max_length=100, verbose_name='Voix')),
                ('locality', models.CharField(max_length=50, verbose_name='Ville')),
                ('postal_code', models.CharField(max_length=6, verbose_name='Code postale')),
                ('country', models.CharField(max_length=50, verbose_name='Pays')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')),
                ('state', models.BooleanField()),
                ('duration', models.CharField(max_length=10)),
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='car', to='car.Car')),
                ('dest_address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dest_adress', to='booking.Address', verbose_name='Adresse de destination')),
                ('start_address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='start_adress', to='booking.Address', verbose_name='Adresse de départ')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
