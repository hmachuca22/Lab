# Generated by Django 2.2 on 2021-10-10 04:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20211009_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aldea',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 9, 22, 25, 45, 320883)),
        ),
        migrations.AlterField(
            model_name='aldea',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 9, 22, 25, 45, 320883)),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 9, 22, 25, 45, 320883)),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 9, 22, 25, 45, 320883)),
        ),
        migrations.AlterField(
            model_name='centroeducativo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 9, 22, 25, 45, 320883)),
        ),
        migrations.AlterField(
            model_name='centroeducativo',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 9, 22, 25, 45, 320883)),
        ),
        migrations.AlterField(
            model_name='corriente',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 9, 22, 25, 45, 320883)),
        ),
        migrations.AlterField(
            model_name='corriente',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 9, 22, 25, 45, 320883)),
        ),
        migrations.AlterField(
            model_name='escrutinio',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 9, 22, 25, 45, 320883)),
        ),
        migrations.AlterField(
            model_name='escrutinio',
            name='mesa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mesa_votos', to='main.CentroEducativo'),
        ),
        migrations.AlterField(
            model_name='escrutinio',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 9, 22, 25, 45, 320883)),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 9, 22, 25, 45, 320883)),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 9, 22, 25, 45, 320883)),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 9, 22, 25, 45, 320883)),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 9, 22, 25, 45, 320883)),
        ),
    ]
