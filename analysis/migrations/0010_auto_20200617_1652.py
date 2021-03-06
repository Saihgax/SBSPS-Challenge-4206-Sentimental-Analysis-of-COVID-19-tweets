# Generated by Django 3.0.7 on 2020-06-17 11:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0009_auto_20200617_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultKeyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='keyword',
            name='default_search_keyword',
        ),
        migrations.AlterField(
            model_name='analysis',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 17, 16, 52, 11, 41632)),
        ),
    ]
