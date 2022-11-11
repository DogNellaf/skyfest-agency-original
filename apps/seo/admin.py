from django.contrib import admin

from import_export.admin import ExportMixin

from seo import models
from snippets.admin import BaseModelAdmin


@admin.register(models.Redirect)
class RedirectAdmin(ExportMixin, BaseModelAdmin):
    """Редиректы"""
    list_display = ('old_path', 'new_path', 'status_code', 'status', 'created')
    list_display_links = ('old_path', 'new_path')
    list_editable = ('status',)
    list_filter = ('status', 'status_code')
    list_select_related = True
    search_fields = ('old_path', 'new_path')
