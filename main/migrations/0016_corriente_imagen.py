# Generated by Django 2.2 on 2021-03-11 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20210310_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='corriente',
            name='imagen',
            field=models.ImageField(default=1, upload_to='media/corriente'),
            preserve_default=False,
        ),
    ]