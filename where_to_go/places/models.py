from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    short_description = models.TextField(
        blank=True,
        null=True,
        default='', 
        verbose_name='Короткое описание'
    )
    long_description = HTMLField(
        blank=True,
        null=True,
        default='', 
        verbose_name='Длинное описание'
    )
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(verbose_name='Картинка')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images', verbose_name='Место')
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name='Порядок',
        db_index=True
    )

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'Картинка {self.id} для места {self.place.title}'
