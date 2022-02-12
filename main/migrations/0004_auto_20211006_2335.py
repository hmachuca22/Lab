# Generated by Django 2.2 on 2021-10-07 05:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211006_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aldea',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 35, 56, 61083)),
        ),
        migrations.AlterField(
            model_name='aldea',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 35, 56, 61083)),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 35, 56, 61083)),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 35, 56, 61083)),
        ),
        migrations.AlterField(
            model_name='centroeducativo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 35, 56, 61083)),
        ),
        migrations.AlterField(
            model_name='centroeducativo',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 35, 56, 61083)),
        ),
        migrations.AlterField(
            model_name='corriente',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 35, 56, 61083)),
        ),
        migrations.AlterField(
            model_name='corriente',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 35, 56, 61083)),
        ),
        migrations.AlterField(
            model_name='escrutinio',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 35, 56, 61083)),
        ),
        migrations.AlterField(
            model_name='escrutinio',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 35, 56, 61083)),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 35, 56, 61083)),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 35, 56, 61083)),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 35, 56, 61083)),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 35, 56, 61083)),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 35, 56, 61083)),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 35, 56, 61083)),
        ),
    ]