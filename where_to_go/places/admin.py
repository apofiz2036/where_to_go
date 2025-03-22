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
        return format_html('<img src="{}" style="max-height: 200px; width: auto;" />', obj.image.url)

    image_preview.short_description = 'Превью'


class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ImageInline]


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'type_image', 'image_preview', 'order')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return format_html('<img src="{}" style="max-height: 200px; width: auto;" />', obj.image.url)

    image_preview.short_description = 'Превью'


admin.site.register(Place, PlaceAdmin)
admin.site.register(Image, ImageAdmin)