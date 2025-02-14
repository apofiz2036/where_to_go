from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    description_short = models.TextField(verbose_name='Короткое описание')
    description_long = models.TextField(verbose_name='Длинное название')
    lng = models.FloatField(verbose_name='Долгота')
    lan = models.FloatField(verbose_name='Широта')

    first_image = models.ForeignKey(
        'Image',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='places_first',
        verbose_name='Первая картинка')

    second_image = models.ManyToManyField(
        'Image',
        blank=True,
        related_name='places_second',
        verbose_name='Вторая картинка'
    )

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

    def __str__(self):
        return self.title
