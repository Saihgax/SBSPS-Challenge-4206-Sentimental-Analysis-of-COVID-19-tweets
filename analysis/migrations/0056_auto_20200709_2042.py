# Generated by Django 3.0.8 on 2020-07-09 15:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0055_auto_20200709_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 9, 20, 42, 29, 174548)),
        ),
    ]