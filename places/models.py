from django.db import models
from tinymce.models import HTMLField
import requests
from urllib.parse import urlparse
from django.core.files.base import ContentFile


class Place(models.Model):
    title = models.CharField('Название', max_length=50)
    description_short = models.TextField('Краткое описание', max_length=250)
    description_long = HTMLField('Полное описание')
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField('Изображение')
    position = models.IntegerField('Позиция', null=True, db_index=True)
    place = models.ForeignKey(verbose_name='Место', to=Place, on_delete=models.PROTECT, related_name='images')

    def save_img_from_url(self, url):
        response = requests.get(url)
        img_name = urlparse(url).path.split('/')[-1]
        self.image.save(name=f'{img_name}', content=ContentFile(response.content), save=True)

    def __str__(self):
        return f'{self.position} {self.place.title}'

    class Meta:
        ordering = ['position']
