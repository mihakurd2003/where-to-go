from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from .forms import FullDescForm


class ImageInline(SortableInlineAdminMixin, admin.StackedInline):
    model = Image
    readonly_fields = ['photo']
    fields = ['image', 'photo', 'position']
    extra = 0

    def photo(self, obj):
        return format_html(
            f'<img src="{obj.image.url}" width="{obj.image.width // 5}" height="{obj.image.height // 5}"/>'
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
    readonly_fields = ['photo']

    def photo(self, obj):
        return format_html(
            f'<img src="{obj.image.url}" width="{obj.image.width // 4}" height="{obj.image.height // 4}"'
        )
