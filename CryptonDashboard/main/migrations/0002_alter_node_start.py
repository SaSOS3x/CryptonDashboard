# Generated by Django 4.2 on 2023-05-19 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='start',
            field=models.IntegerField(max_length=250, verbose_name='Дата старта проекта'),
        ),
    ]
