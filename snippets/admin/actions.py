from snippets.choices import StatusChoices


def activate(modeladmin, request, queryset):
    queryset.update(is_active=True)


activate.short_description = 'Активировать'


def deactivate(modeladmin, request, queryset):
    queryset.update(is_active=False)


deactivate.short_description = 'Деактивировать'


def draft(modeladmin, request, queryset):
    queryset.update(status=StatusChoices.DRAFT.value)


draft.short_description = 'В черновики'


def hide(modeladmin, request, queryset):
    queryset.update(status=StatusChoices.HIDDEN.value)


hide.short_description = 'Скрыть'


def publish(modeladmin, request, queryset):
    queryset.update(status=StatusChoices.PUBLIC.value)


publish.short_description = 'Опубликовать'
