from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    description_short = models.TextField(verbose_name='Короткое описание')
    description_long = HTMLField(verbose_name='Длинное название')
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    TYPE_IMAGE = [
        ('first_image', 'Первая картинка'),
        ('second_image', 'Вторая картинка')
    ]

    title = models.CharField(max_length=100, verbose_name='Название картинки')
    type_image = models.CharField(max_length=50, choices=TYPE_IMAGE, verbose_name='тип картинки')
    image = models.ImageField(verbose_name='Картинка')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images', null=True, blank=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name='порядок')

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
