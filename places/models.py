from django.db import models


class Image(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    imgs = models.ImageField(verbose_name='Фото', blank=True, upload_to='media/')

    def __str__(self):
        return f'{self.pk} {self.title}'

class Place(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    description_short = models.TextField(verbose_name='Краткое описание', blank=True)
    description_long = models.TextField(verbose_name='Полное описание', blank=True)
    lat = models.FloatField(verbose_name='Широта')
    lng = models.FloatField(verbose_name='Долгота')
    place_imgs = models.ForeignKey(Image, verbose_name='Фотографии', related_name='place_imgs', blank=True, null=True,
                                   on_delete=models.CASCADE)

    def __str__(self):
        return self.title



