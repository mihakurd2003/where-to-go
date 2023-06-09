from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=150)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = HTMLField('Полное описание', blank=True)
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField('Изображение')
    position = models.IntegerField('Позиция', null=True, db_index=True)
    place = models.ForeignKey(
        verbose_name='Место',
        to=Place,
        on_delete=models.CASCADE,
        related_name='images'
    )

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f'{self.position} {self.place.title}'
