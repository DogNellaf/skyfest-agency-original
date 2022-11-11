from snippets.template_backends.jinja2 import jinjaglobal, jinjafilter
from vars import models
from vars.db_config import db_vars
from vars.site_config import site_config


@jinjaglobal
def get_site_config():
    return site_config.all()


@jinjafilter
def preprocess_content(content):
    if '<table' not in content:
        return content

    content = content.replace('<table', '<div class="table-wrap"><table')\
        .replace('</table>', '</table></div>')

    return content


@jinjaglobal
def menu(menu_slug):
    try:
        menu_obj = models.Menu.objects.published().get(slug=menu_slug)
    except models.Menu.DoesNotExist:
        return None

    return menu_obj, menu_obj.items.published().order_by('ordering')


@jinjaglobal
def menu_items(menu_slug):
    try:
        menu_obj = models.Menu.objects.published().get(slug=menu_slug)
    except models.Menu.DoesNotExist:
        return []

    return menu_obj.items.published().order_by('ordering')


@jinjaglobal
def var(key, request, **kwargs):
    result = db_vars.get(key, request.LANGUAGE_CODE, '')
    if kwargs:
        result = result.format(**kwargs)
    return result
