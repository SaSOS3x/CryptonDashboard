# Generated by Django 4.2 on 2023-05-19 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_node_start'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='about',
            field=models.TextField(default='nothing', verbose_name='Описание'),
        ),
    ]