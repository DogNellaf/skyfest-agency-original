from django.conf import settings
from django.urls import reverse
from django.utils.translation import ugettext_lazy

from snippets.template_backends.jinja2 import jinjaglobal


@jinjaglobal
def lang_url(route_name, *args, **kwargs):
    new_kwargs = kwargs.copy()

    if 'lang' in new_kwargs:
        if new_kwargs['lang'] == settings.LANGUAGE_CODE:
            del new_kwargs['lang']

    if kwargs['lang'] != settings.LANGUAGE_CODE:
        route_name += '_lang'

    return reverse(route_name, args=args, kwargs=new_kwargs)


@jinjaglobal
def get_language_href(request, lang):
    match = request.resolver_match
    new_kwargs = match.kwargs.copy()
    url_name = match.url_name
    if lang == settings.LANGUAGE_CODE:
        if 'lang' in new_kwargs:
            del new_kwargs['lang']
        if url_name.endswith('_lang'):
            url_name = url_name.replace('_lang', '')
    else:
        if not url_name.endswith('_lang'):
            url_name += '_lang'
        new_kwargs['lang'] = lang

    query = ''
    if request.GET:
        query = '?' + request.GET.urlencode()
    url = reverse(f'{match.namespace}:{url_name}', args=match.args, kwargs=new_kwargs) + query
    return url


@jinjaglobal
def get_languages(request):
    return [{
        'code': x[0],
        'name': x[1],
        'href': get_language_href(request, x[0])
    } for x in settings.LANGUAGES if x[0] in settings.LANGUAGE_CODES_PUBLIC]


@jinjaglobal
def ugettext(value):
    return ugettext_lazy(value)
