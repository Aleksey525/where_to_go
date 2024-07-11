from django.contrib import admin
from .models import Place, Image
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableTabularInline, SortableAdminBase

class ImageTabularInline(SortableTabularInline):
    model = Image
    fields = ('title', 'img', 'preview', 'position')
    readonly_fields = ['preview']

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" style="max-height: 200px;">')
@admin.register(Place)
class SortablePlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageTabularInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass




