# Generated by Django 2.2 on 2021-10-07 13:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211006_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aldea',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 7, 46, 32, 235070)),
        ),
        migrations.AlterField(
            model_name='aldea',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 7, 46, 32, 235070)),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 7, 46, 32, 235070)),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 7, 46, 32, 235070)),
        ),
        migrations.AlterField(
            model_name='centroeducativo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 7, 46, 32, 235070)),
        ),
        migrations.AlterField(
            model_name='centroeducativo',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 7, 46, 32, 235070)),
        ),
        migrations.AlterField(
            model_name='corriente',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 7, 46, 32, 235070)),
        ),
        migrations.AlterField(
            model_name='corriente',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 7, 46, 32, 235070)),
        ),
        migrations.AlterField(
            model_name='escrutinio',
            name='centro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.CentroEducativo', verbose_name='Centro de Votación'),
        ),
        migrations.AlterField(
            model_name='escrutinio',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 7, 46, 32, 235070)),
        ),
        migrations.AlterField(
            model_name='escrutinio',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 7, 46, 32, 235070)),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 7, 46, 32, 235070)),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 7, 46, 32, 235070)),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 7, 46, 32, 235070)),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 7, 46, 32, 235070)),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 7, 46, 32, 235070)),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 7, 7, 46, 32, 235070)),
        ),
    ]
