# Generated by Django 4.2.6 on 2024-07-22 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='Название'),
        ),
    ]
