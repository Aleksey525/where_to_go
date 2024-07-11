from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    description_short = models.TextField(verbose_name='Краткое описание', blank=True)
    description_long = tinymce_models.HTMLField(verbose_name='Полное описание', blank=True)
    lat = models.FloatField(verbose_name='Широта')
    lng = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Image(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    img = models.ImageField(verbose_name='Фото', blank=True)
    place = models.ForeignKey(Place, null=True, blank=True, on_delete=models.CASCADE)
    position = models.PositiveIntegerField(verbose_name='Позиция', default=0)

    def __str__(self):
        return f'{self.pk} {self.title}'

    def save(self, *args, **kwargs):
        if not self.position:
            last_image = Image.objects.filter(place=self.place).order_by('-position').first()
            if last_image is None:
                self.position = 0
            else:
                self.position = last_image.position + 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['position']
