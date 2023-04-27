from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from .forms import FullDescForm


class ImageInline(SortableInlineAdminMixin, admin.StackedInline):
    model = Image
    readonly_fields = ['add_photo']
    fields = ['image', 'add_photo', 'position']
    extra = 0

    def add_photo(self, image_obj):
        return format_html(
            '<img src="{}" style="max-height: {};"/>',
            image_obj.image.url,
            '200px'
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline]
    form = FullDescForm

    class Media:
        js = ['adminsortable2/js/jquery-ui.min.js', 'adminsortable2/js/admin.sortable.min.js']
        css = {'all': ('adminsortable2/css/admin.sortable.css',)}


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ['add_photo']

    def add_photo(self, image_obj):
        return format_html(
            '<img src="{}" style="max-height: {};"/>',
            image_obj.image.url,
            '200px'
        )
