# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-18 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0004_auto_20171121_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='priority',
            field=models.CharField(choices=[('minor', 'Незначительная'), ('normal', 'Обычная'), ('major', 'Важная'), ('critical', 'Критическая')], default='normal', max_length=255, verbose_name='приоритет'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('open', 'Открыта'), ('in_progress', 'В разработке'), ('testing', 'В тестировании'), ('production', 'На боевом сервере'), ('closed', 'Закрыта')], default='open', max_length=255, verbose_name='статус'),
        ),
    ]
