# Generated by Django 2.0.7 on 2018-08-26 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KIA_services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kiaservicefield',
            name='service',
        ),
        migrations.RemoveField(
            model_name='kiatransaction',
            name='assigned_emp',
        ),
        migrations.RemoveField(
            model_name='kiatransaction',
            name='service',
        ),
        migrations.RemoveField(
            model_name='kiatransaction',
            name='user',
        ),
        migrations.DeleteModel(
            name='KIAService',
        ),
        migrations.DeleteModel(
            name='KIAServiceField',
        ),
        migrations.DeleteModel(
            name='KIATransaction',
        ),
    ]
