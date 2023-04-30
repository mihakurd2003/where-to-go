from django.contrib import admin
from .models import Place, Image
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from .forms import FullDescForm
from .get_photo import GetPhoto


class ImageInline(SortableInlineAdminMixin, admin.StackedInline, GetPhoto):
    model = Image
    readonly_fields = ['get_photo']
    fields = ['image', 'get_photo', 'position']
    extra = 0


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline]
    form = FullDescForm

    class Media:
        js = [
            'adminsortable2/js/jquery-ui.min.js',
            'adminsortable2/js/admin.sortable.min.js'
        ]
        css = {'all': ('adminsortable2/css/admin.sortable.css',)}


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin, GetPhoto):
    readonly_fields = ['get_photo']
