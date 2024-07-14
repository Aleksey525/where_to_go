from django.contrib import admin
from django.utils.safestring import mark_safe

from adminsortable2.admin import SortableTabularInline, SortableAdminBase

from .models import Place, Image

class ImageTabularInline(SortableTabularInline):
    model = Image
    fields = ('title', 'img', 'preview', 'position')
    readonly_fields = ['preview']

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" style="max-height: 200px;">')


@admin.register(Place)
class SortablePlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    search_fields = ['title']
    inlines = [
        ImageTabularInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass





