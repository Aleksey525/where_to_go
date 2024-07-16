from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    short_description = models.TextField(verbose_name='Краткое описание', blank=True)
    long_description = tinymce_models.HTMLField(verbose_name='Полное описание', blank=True)
    lat = models.FloatField(verbose_name='Широта')
    lng = models.FloatField(verbose_name='Долгота')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title


class Image(models.Model):
    img = models.ImageField(verbose_name='Фото')
    place = models.ForeignKey(Place, null=True, on_delete=models.CASCADE)
    position = models.PositiveIntegerField(verbose_name='Позиция', default=0)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['position']

    def __str__(self):
        return f'{self.pk}'


