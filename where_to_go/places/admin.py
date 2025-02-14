from django.contrib import admin
from .models import Place, Image


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'type_image')


admin.site.register(Place, PlaceAdmin)
admin.site.register(Image, ImageAdmin)