# Generated by Django 2.0.7 on 2018-08-26 05:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KIA_admin', '0009_auto_20180826_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historyofadminactivities',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 8, 26, 5, 0, 25, 407748)),
        ),
    ]
