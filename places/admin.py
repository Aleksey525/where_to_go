from django.contrib import admin
from .models import Place, Image
from django.utils.safestring import mark_safe

class ImageInline(admin.TabularInline):
    model = Image
    fields = ['title', 'imgs', 'preview', 'position']
    readonly_fields = ['preview']
    def preview(self, obj):
        return mark_safe(f'<img src="{obj.imgs.url}" style="max-height: 200px;">')


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Place, PlaceAdmin)
admin.site.register(Image)
