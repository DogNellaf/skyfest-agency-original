from django.http.response import Http404
from django.shortcuts import get_object_or_404

from pages import models
from snippets.choices import StatusChoices


def get_flat_page(slug, raise_error=True):
    """Получает простую страницу по алиасу"""
    try:
        page = get_object_or_404(
            models.FlatPage, slug__exact=slug, status=StatusChoices.PUBLIC.value
        )
    except Http404 as e:
        if raise_error:
            raise e
        else:
            page = None
    return page
