# Generated by Django 3.1.2 on 2020-11-06 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0006_auto_20201105_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sumcorona',
            name='domestic',
        ),
        migrations.RemoveField(
            model_name='sumcorona',
            name='oversea',
        ),
    ]
