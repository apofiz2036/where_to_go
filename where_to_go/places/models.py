from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    description_short = models.TextField(verbose_name='Короткое описание')
    description_long = models.TextField(verbose_name='Длинное название')
    lng = models.FloatField(verbose_name='Долгота')
    lan = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title
    
