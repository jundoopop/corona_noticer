# Generated by Django 3.1.2 on 2020-11-09 05:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('cases', '0008_remove_dailycorona_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sumcorona',
            name='date',
            field=models.DateField(primary_key=True, serialize=False),
        ),
    ]
