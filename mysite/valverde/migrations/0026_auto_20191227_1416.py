# Generated by Django 2.2.5 on 2019-12-27 13:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('valverde', '0025_auto_20191227_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pic_nr',
            field=models.IntegerField(blank=True, default=9),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 27, 13, 16, 21, 569561, tzinfo=utc)),
        ),
    ]