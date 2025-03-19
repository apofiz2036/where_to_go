from django.contrib import admin
from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ImageInline]


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'type_image')


admin.site.register(Place, PlaceAdmin)
admin.site.register(Image, ImageAdmin)