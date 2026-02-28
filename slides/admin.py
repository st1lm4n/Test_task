from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from django.utils.html import format_html
from .models import Slide

@admin.register(Slide)
class SlideAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('thumb', 'title', 'is_active', 'order')
    list_editable = ('is_active',)
    search_fields = ('title',)
    list_display_links = ('title',)
    fieldsets = (
        (None, {'fields': ('title', 'image', 'is_active', 'order')}),
    )
    ordering = ('order',)

    def thumb(self, obj):
        if obj.image_id:
            try:
                url = obj.image.url
                return format_html('<img src="{}" style="height:60px; border-radius:4px;" />', url)
            except Exception:
                return '—'
        return '—'
    thumb.short_description = 'Превью'