from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Place, Image
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return format_html('<img src="{}" style="max-height: 200px; max-width: 200px;" />', obj.image.url)

    image_preview.short_description = 'Превью'


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ImageInline]
    search_fields = ['title']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'order')
    readonly_fields = ('image_preview',)
    autocomplete_fields = ['place']

    def image_preview(self, obj):
        return format_html('<img src="{}" style="max-height: 200px; max-width: 200px;" />', obj.image.url)

    image_preview.short_description = 'Превью'
