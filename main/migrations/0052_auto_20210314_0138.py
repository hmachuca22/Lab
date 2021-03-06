# Generated by Django 2.2 on 2021-03-14 07:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0051_auto_20210314_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acta',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 14, 1, 38, 9, 133554)),
        ),
        migrations.AlterField(
            model_name='acta',
            name='mesa',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='acta',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 14, 1, 38, 9, 133554)),
        ),
        migrations.AlterField(
            model_name='aldea',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 14, 1, 38, 9, 133554)),
        ),
        migrations.AlterField(
            model_name='aldea',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 14, 1, 38, 9, 133554)),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 14, 1, 38, 9, 133554)),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 14, 1, 38, 9, 133554)),
        ),
        migrations.AlterField(
            model_name='corriente',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 14, 1, 38, 9, 133554)),
        ),
        migrations.AlterField(
            model_name='corriente',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 14, 1, 38, 9, 133554)),
        ),
        migrations.AlterField(
            model_name='escrutinio',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 14, 1, 38, 9, 133554)),
        ),
        migrations.AlterField(
            model_name='escrutinio',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 14, 1, 38, 9, 133554)),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 14, 1, 38, 9, 133554)),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 14, 1, 38, 9, 133554)),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 14, 1, 38, 9, 133554)),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 14, 1, 38, 9, 133554)),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 14, 1, 38, 9, 133554)),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 14, 1, 38, 9, 133554)),
        ),
        migrations.DeleteModel(
            name='BalanceGeneral',
        ),
    ]
