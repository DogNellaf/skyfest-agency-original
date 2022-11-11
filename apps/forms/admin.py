from django.contrib import admin
from django.contrib.admin.exceptions import DisallowedModelAdminToField
from django.contrib.admin.options import TO_FIELD_VAR
from django.contrib.admin.utils import unquote

from forms import models
from forms.choices import FormRequestReadStatusChoices


class BaseFormRequestAdmin(admin.ModelAdmin):
    """Base class for form request"""
    date_hierarchy = 'created'
    list_display = ('id', 'language', 'updated')
    list_filter = ('read_status', 'language')
    ordering = ('-created',)
    readonly_fields = ('created', 'updated')
    search_fields = ('=id',)

    @staticmethod
    def suit_row_attributes(obj, request):
        return {'class': 'is-unread' if obj.read_status < 0 else 'is-read'}

    def change_view(self, request, object_id, form_url='', extra_context=None):
        """Marks object read"""
        if object_id:

            to_field = request.POST.get(TO_FIELD_VAR, request.GET.get(TO_FIELD_VAR))
            if to_field and not self.to_field_allowed(request, to_field):
                raise DisallowedModelAdminToField("The field %s cannot be referenced." % to_field)

            obj = self.get_object(request, unquote(object_id), to_field)
            if obj and obj.read_status < 0:
                obj.read_status = FormRequestReadStatusChoices.READ.value
                obj.save()

        return super(BaseFormRequestAdmin, self).change_view(
            request, object_id, form_url=form_url, extra_context=extra_context
        )


@admin.register(models.Feedback)
class FeedbackAdmin(BaseFormRequestAdmin):
    """Обратная связь"""

    fields = models.Feedback().collect_fields()
    list_display = ('id', 'name', 'phone_number', 'email', 'created')
    list_display_links = ('id', 'name', 'phone_number', 'email')
    list_filter = BaseFormRequestAdmin.list_filter + ('url',)
    search_fields = BaseFormRequestAdmin.search_fields + (
        'name', 'phone_number', 'email', 'comment', 'url'
    )


@admin.register(models.Order)
class OrderAdmin(BaseFormRequestAdmin):
    """Заказы"""

    fields = models.Order().collect_fields()
    list_display = ('id', 'name', 'phone_number', 'email', 'role', 'created')
    list_display_links = ('id', 'name', 'phone_number', 'email')
    list_filter = BaseFormRequestAdmin.list_filter + ('role', 'url')
    search_fields = BaseFormRequestAdmin.search_fields + (
        'name', 'phone_number', 'email', 'comment', 'role__title', 'url'
    )


@admin.register(models.Subscribe)
class SubscribeAdmin(BaseFormRequestAdmin):
    """Подписки"""

    fields = models.Subscribe().collect_fields()
    list_display = ('id', 'email', 'created')
    list_display_links = ('id', 'email')
    search_fields = BaseFormRequestAdmin.search_fields + ('email',)
