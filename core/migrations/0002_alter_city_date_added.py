# Generated by Django 3.2.12 on 2022-04-19 15:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 19, 16, 38, 28, 643851)),
        ),
    ]
