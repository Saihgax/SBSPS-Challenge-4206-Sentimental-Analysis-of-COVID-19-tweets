# Generated by Django 3.0.8 on 2020-07-06 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constants', '0002_noofpopulartweets'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoOfTrendingKeywords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
            ],
        ),
    ]
