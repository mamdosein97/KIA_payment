# Generated by Django 2.0.3 on 2018-08-18 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kia_services', '0005_auto_20180818_1231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kiaservice',
            name='label',
        ),
    ]