# Generated by Django 2.0.7 on 2018-08-27 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KIA_admin', '0018_auto_20180826_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsMessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=32)),
                ('sender_phone_number', models.CharField(max_length=11)),
                ('sender_email', models.CharField(max_length=64)),
                ('message', models.CharField(max_length=256)),
            ],
        ),
    ]