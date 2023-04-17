from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=50)
    description_short = models.TextField('Краткое описание', max_length=250)
    description_long = models.TextField('Полное описание')
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title
