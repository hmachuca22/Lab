# Generated by Django 2.2 on 2021-02-20 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210219_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='acta',
            name='aldea',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
