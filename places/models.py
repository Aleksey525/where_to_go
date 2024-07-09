from django.db import models


class Place(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    description_short = models.TextField(verbose_name='Краткое описание', blank=True)
    description_long = models.TextField(verbose_name='Полное описание', blank=True)
    lat = models.FloatField(verbose_name='Широта')
    lng = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Image(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    imgs = models.ImageField(verbose_name='Фото', blank=True, upload_to='media/')
    place = models.ForeignKey(Place, blank=True, null=True, on_delete=models.CASCADE)
    position = models.IntegerField(verbose_name='Позиция', null=True, blank=True)

    def __str__(self):
        return f'{self.pk} {self.title}'

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'





