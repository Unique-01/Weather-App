# Generated by Django 3.2.12 on 2022-04-26 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_city_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='title',
            new_name='cityname',
        ),
    ]