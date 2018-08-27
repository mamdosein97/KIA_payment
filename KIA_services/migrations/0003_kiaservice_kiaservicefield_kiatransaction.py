# Generated by Django 2.0.7 on 2018-08-26 07:46

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('KIA_auth', '0007_auto_20180824_1213'),
        ('KIA_services', '0002_auto_20180826_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='KIAService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=100, null=True)),
                ('currency', models.IntegerField(choices=[(1, 'دلار'), (2, 'یورو'), (3, 'پوند')], default=1)),
                ('variable_price', models.BooleanField(default=False)),
                ('price', models.IntegerField(null=True)),
                ('details', models.TextField()),
                ('image_url', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KIAServiceField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('label', models.CharField(max_length=100)),
                ('type', models.IntegerField(choices=[(2, 'فیلد متنی'), (3, 'فیلد انتخاب یک گزینه'), (5, 'فیلد تاریخ'), (6, 'فیلد تاریخ و زمان'), (7, 'فیلد عدد اعشاری'), (9, 'فیلد ایمیل'), (10, 'فیلد فایل'), (13, 'فیلد عدد صحیح'), (14, 'فیلد انتخاب چند گزینه')])),
                ('optional', models.BooleanField(default=False)),
                ('args', jsonfield.fields.JSONField(null=True)),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='KIA_services.KIAService')),
            ],
        ),
        migrations.CreateModel(
            name='KIATransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(choices=[(1, 'ثبت شده'), (2, 'در حال انجام'), (3, 'تمام شده'), (4, 'رد شده'), (5, 'مشکوک')])),
                ('register_time', models.DateTimeField(null=True)),
                ('cost_in_rial', models.IntegerField(null=True)),
                ('data', jsonfield.fields.JSONField()),
                ('assigned_emp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='emp_transactions', to='KIA_auth.Profile')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='KIA_services.KIAService')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_transactions', to='KIA_auth.Profile')),
            ],
        ),
    ]
