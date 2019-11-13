# Generated by Django 2.2.5 on 2019-11-11 12:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('valverde', '0003_auto_20191111_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='valverde/static/valverde/post_images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 11, 12, 26, 31, 993892, tzinfo=utc)),
        ),
    ]