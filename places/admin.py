from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ['photo']
    fields = ['image', 'photo', 'position']

    def photo(self, obj):
        return format_html(
            f'<img src="{obj.image.url}" width="{obj.image.width // 4}" height="{obj.image.height // 4}"/>'
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ['photo']

    def photo(self, obj):
        return format_html(
            f'<img src="{obj.image.url}" width="{obj.image.width // 3}" height="{obj.image.height // 3}"'
        )
