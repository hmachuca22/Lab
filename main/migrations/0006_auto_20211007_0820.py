# Generated by Django 2.2 on 2021-10-07 14:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20211007_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='centroeducativo',
            name='codigo',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='centroeducativo',
            name='nombre',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aldea',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 8, 20, 3, 621084)),
        ),
        migrations.AlterField(
            model_name='aldea',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 8, 20, 3, 621084)),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 8, 20, 3, 621084)),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 8, 20, 3, 621084)),
        ),
        migrations.AlterField(
            model_name='centroeducativo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 8, 20, 3, 621084)),
        ),
        migrations.AlterField(
            model_name='centroeducativo',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 8, 20, 3, 621084)),
        ),
        migrations.AlterField(
            model_name='corriente',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 8, 20, 3, 621084)),
        ),
        migrations.AlterField(
            model_name='corriente',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 8, 20, 3, 621084)),
        ),
        migrations.AlterField(
            model_name='escrutinio',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 8, 20, 3, 621084)),
        ),
        migrations.AlterField(
            model_name='escrutinio',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 8, 20, 3, 621084)),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 8, 20, 3, 621084)),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 8, 20, 3, 621084)),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 8, 20, 3, 621084)),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 8, 20, 3, 621084)),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 8, 20, 3, 621084)),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 8, 20, 3, 621084)),
        ),
    ]
