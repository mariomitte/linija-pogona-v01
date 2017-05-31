# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 19:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pogon', '0002_pwm'),
    ]

    operations = [
        migrations.AddField(
            model_name='pwm',
            name='korisnik',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pwm',
            name='period',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='pwm',
            name='sirina',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]