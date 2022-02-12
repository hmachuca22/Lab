# Generated by Django 2.2 on 2021-03-14 00:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_auto_20210313_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='departamento_candidato',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='departamento_candidatos', to='main.Departamento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidato',
            name='municipio_candidato',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='municipio_candidatos', to='main.Municipio'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='acta',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 42, 3, 283875)),
        ),
        migrations.AlterField(
            model_name='acta',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 42, 3, 283875)),
        ),
        migrations.AlterField(
            model_name='aldea',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 42, 3, 283875)),
        ),
        migrations.AlterField(
            model_name='aldea',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 42, 3, 283875)),
        ),
        migrations.AlterField(
            model_name='balancegeneral',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 42, 3, 283875)),
        ),
        migrations.AlterField(
            model_name='balancegeneral',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 42, 3, 283875)),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 42, 3, 283875)),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 42, 3, 283875)),
        ),
        migrations.AlterField(
            model_name='corriente',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 42, 3, 283875)),
        ),
        migrations.AlterField(
            model_name='corriente',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 42, 3, 283875)),
        ),
        migrations.AlterField(
            model_name='escrutinio',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 42, 3, 283875)),
        ),
        migrations.AlterField(
            model_name='escrutinio',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 42, 3, 283875)),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 42, 3, 283875)),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 42, 3, 283875)),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 42, 3, 283875)),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 42, 3, 283875)),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 42, 3, 283875)),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 18, 42, 3, 283875)),
        ),
    ]
