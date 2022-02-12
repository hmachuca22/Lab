# Generated by Django 2.2 on 2021-03-14 00:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_auto_20210313_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='municipio',
            name='departamento',
        ),
        migrations.AlterField(
            model_name='acta',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 41, 32, 405346)),
        ),
        migrations.AlterField(
            model_name='acta',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 41, 32, 406345)),
        ),
        migrations.AlterField(
            model_name='aldea',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 41, 32, 405346)),
        ),
        migrations.AlterField(
            model_name='aldea',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 41, 32, 406345)),
        ),
        migrations.AlterField(
            model_name='balancegeneral',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 41, 32, 405346)),
        ),
        migrations.AlterField(
            model_name='balancegeneral',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 41, 32, 406345)),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 41, 32, 405346)),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 41, 32, 406345)),
        ),
        migrations.AlterField(
            model_name='corriente',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 41, 32, 405346)),
        ),
        migrations.AlterField(
            model_name='corriente',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 41, 32, 406345)),
        ),
        migrations.AlterField(
            model_name='escrutinio',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 41, 32, 405346)),
        ),
        migrations.AlterField(
            model_name='escrutinio',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 41, 32, 406345)),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 41, 32, 405346)),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 41, 32, 406345)),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 41, 32, 405346)),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 41, 32, 406345)),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 41, 32, 405346)),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 41, 32, 406345)),
        ),
    ]
