# Generated by Django 3.0.8 on 2020-07-08 06:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0047_auto_20200708_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 8, 12, 29, 18, 232946)),
        ),
    ]