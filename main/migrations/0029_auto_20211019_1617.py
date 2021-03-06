# Generated by Django 2.2 on 2021-10-19 16:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20211019_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aldea',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 19, 16, 17, 33, 48453)),
        ),
        migrations.AlterField(
            model_name='aldea',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 19, 16, 17, 33, 48453)),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 19, 16, 17, 33, 48453)),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 19, 16, 17, 33, 48453)),
        ),
        migrations.AlterField(
            model_name='centroeducativo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 19, 16, 17, 33, 48453)),
        ),
        migrations.AlterField(
            model_name='centroeducativo',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 19, 16, 17, 33, 48453)),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 19, 16, 17, 33, 48453)),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 19, 16, 17, 33, 48453)),
        ),
        migrations.AlterField(
            model_name='corriente',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 19, 16, 17, 33, 48453)),
        ),
        migrations.AlterField(
            model_name='corriente',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 19, 16, 17, 33, 48453)),
        ),
        migrations.AlterField(
            model_name='escrutinio',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 19, 16, 17, 33, 48453)),
        ),
        migrations.AlterField(
            model_name='escrutinio',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 19, 16, 17, 33, 48453)),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 19, 16, 17, 33, 48453)),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 19, 16, 17, 33, 48453)),
        ),
        migrations.AlterField(
            model_name='partido',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 19, 16, 17, 33, 48453)),
        ),
        migrations.AlterField(
            model_name='partido',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 19, 16, 17, 33, 48453)),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 19, 16, 17, 33, 48453)),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 19, 16, 17, 33, 48453)),
        ),
    ]
