# Generated by Django 2.1.7 on 2019-04-11 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0011_auto_20190411_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
