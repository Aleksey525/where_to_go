from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import format_html

from adminsortable2.admin import SortableTabularInline, SortableAdminBase

from .models import Place, Image

class ImageTabularInline(SortableTabularInline):
    model = Image
    fields = ('img', 'preview', 'position')
    readonly_fields = ['preview']

    def preview(self, obj):
        return format_html('<img src="{}" style="max-height: 200px;">', mark_safe(obj.img.url))


@admin.register(Place)
class SortablePlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    search_fields = ['title']
    inlines = [
        ImageTabularInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass





