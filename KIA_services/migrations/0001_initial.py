# Generated by Django 2.0.3 on 2018-08-10 11:09

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KIAService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='KIAServiceField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('type', models.IntegerField(choices=[(1, 'BooleanField'), (2, 'CharField'), (3, 'CharField'), (4, 'TypedChoiceField'), (5, 'DateField'), (6, 'DateTimeField'), (7, 'DecimalField'), (8, 'DurationField '), (9, 'EmailField'), (10, 'FileField'), (11, 'FilePathField'), (12, 'ImageField'), (13, 'IntegerField'), (14, 'MultipleChoiceField'), (15, 'TypedMultipleChoiceField'), (16, 'ComboField')])),
                ('args', jsonfield.fields.JSONField()),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='KIA_services.KIAService')),
            ],
        ),
    ]
