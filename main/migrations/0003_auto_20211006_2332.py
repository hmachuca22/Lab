# Generated by Django 2.2 on 2021-10-07 05:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_auto_20211006_2241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='escrutinio',
            name='corriente',
        ),
        migrations.RemoveField(
            model_name='escrutinio',
            name='departamento',
        ),
        migrations.RemoveField(
            model_name='escrutinio',
            name='municipio',
        ),
        migrations.RemoveField(
            model_name='escrutinio',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='escrutinio',
            name='tipo_escrutinio',
        ),
        migrations.AlterField(
            model_name='aldea',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 31, 57, 748487)),
        ),
        migrations.AlterField(
            model_name='aldea',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 31, 57, 748487)),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 31, 57, 748487)),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 31, 57, 748487)),
        ),
        migrations.AlterField(
            model_name='corriente',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 31, 57, 748487)),
        ),
        migrations.AlterField(
            model_name='corriente',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 31, 57, 748487)),
        ),
        migrations.AlterField(
            model_name='escrutinio',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 31, 57, 748487)),
        ),
        migrations.AlterField(
            model_name='escrutinio',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 31, 57, 748487)),
        ),
        migrations.AlterField(
            model_name='escrutinio',
            name='valor',
            field=models.IntegerField(max_length=15),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 31, 57, 748487)),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 31, 57, 748487)),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 31, 57, 748487)),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='numero',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 31, 57, 748487)),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 31, 57, 748487)),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 31, 57, 748487)),
        ),
        migrations.CreateModel(
            name='CentroEducativo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 31, 57, 748487))),
                ('update_at', models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 23, 31, 57, 748487))),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departamento_centroeducativo', to='main.Departamento')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='municipio_centroeducativo', to='main.Municipio')),
                ('user_created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='centroeducativo_requests_user_created', to=settings.AUTH_USER_MODEL)),
                ('user_update', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='centroeducativo_requests_user_update', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='escrutinio',
            name='centro',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.CentroEducativo'),
            preserve_default=False,
        ),
    ]
