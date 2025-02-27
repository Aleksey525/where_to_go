# Generated by Django 4.2.6 on 2024-07-18 14:42

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('short_description', models.TextField(blank=True, verbose_name='Краткое описание')),
                ('long_description', tinymce.models.HTMLField(blank=True, verbose_name='Полное описание')),
                ('lat', models.FloatField(verbose_name='Широта')),
                ('lng', models.FloatField(verbose_name='Долгота')),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='', verbose_name='Фото')),
                ('position', models.PositiveIntegerField(db_index=True, default=0, verbose_name='Позиция')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
                'ordering': ['position'],
            },
        ),
    ]
