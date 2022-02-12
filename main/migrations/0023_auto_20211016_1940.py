# Generated by Django 2.2 on 2021-10-16 19:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20211015_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='partido',
            name='logo',
            field=models.ImageField(default=1, upload_to='media/corriente'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aldea',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 16, 19, 40, 38, 554469)),
        ),
        migrations.AlterField(
            model_name='aldea',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 16, 19, 40, 38, 554469)),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 16, 19, 40, 38, 554469)),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 16, 19, 40, 38, 554469)),
        ),
        migrations.AlterField(
            model_name='centroeducativo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 16, 19, 40, 38, 554469)),
        ),
        migrations.AlterField(
            model_name='centroeducativo',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 16, 19, 40, 38, 554469)),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 16, 19, 40, 38, 554469)),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 16, 19, 40, 38, 554469)),
        ),
        migrations.AlterField(
            model_name='corriente',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 16, 19, 40, 38, 554469)),
        ),
        migrations.AlterField(
            model_name='corriente',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 16, 19, 40, 38, 554469)),
        ),
        migrations.AlterField(
            model_name='escrutinio',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 16, 19, 40, 38, 554469)),
        ),
        migrations.AlterField(
            model_name='escrutinio',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 16, 19, 40, 38, 554469)),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 16, 19, 40, 38, 554469)),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 16, 19, 40, 38, 554469)),
        ),
        migrations.AlterField(
            model_name='partido',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 16, 19, 40, 38, 554469)),
        ),
        migrations.AlterField(
            model_name='partido',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 16, 19, 40, 38, 554469)),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 16, 19, 40, 38, 554469)),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 16, 19, 40, 38, 554469)),
        ),
    ]
