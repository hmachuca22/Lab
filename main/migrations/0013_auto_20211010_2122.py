# Generated by Django 2.2 on 2021-10-11 03:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20211010_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidato',
            name='corriente',
        ),
        migrations.AddField(
            model_name='candidato',
            name='partido',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Partido'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aldea',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 10, 21, 22, 22, 736482)),
        ),
        migrations.AlterField(
            model_name='aldea',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 10, 21, 22, 22, 736482)),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 10, 21, 22, 22, 736482)),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 10, 21, 22, 22, 736482)),
        ),
        migrations.AlterField(
            model_name='centroeducativo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 10, 21, 22, 22, 736482)),
        ),
        migrations.AlterField(
            model_name='centroeducativo',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 10, 21, 22, 22, 736482)),
        ),
        migrations.AlterField(
            model_name='corriente',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 10, 21, 22, 22, 736482)),
        ),
        migrations.AlterField(
            model_name='corriente',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 10, 21, 22, 22, 736482)),
        ),
        migrations.AlterField(
            model_name='escrutinio',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 10, 21, 22, 22, 736482)),
        ),
        migrations.AlterField(
            model_name='escrutinio',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 10, 21, 22, 22, 736482)),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 10, 21, 22, 22, 736482)),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 10, 21, 22, 22, 736482)),
        ),
        migrations.AlterField(
            model_name='partido',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 10, 21, 22, 22, 736482)),
        ),
        migrations.AlterField(
            model_name='partido',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 10, 21, 22, 22, 736482)),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 10, 21, 22, 22, 736482)),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 10, 21, 22, 22, 736482)),
        ),
    ]
