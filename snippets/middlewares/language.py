from django.conf import settings
from django.http.response import Http404
from django.utils import translation
from django.utils.deprecation import MiddlewareMixin
from django.utils.translation import ugettext_lazy as _


class LanguageMiddleware(MiddlewareMixin):
    """Language middleware"""
    @staticmethod
    def process_view(request, view_func, view_args, view_kwargs):
        lang = request.resolver_match.kwargs.get('lang', settings.DEFAULT_LANGUAGE)
        if len(lang) > 2:
            lang = None

        available_langs = settings.LANGUAGE_CODES_PUBLIC
        if lang not in available_langs:
            raise Http404(_('Язык "%s" не зарегистрирован в системе') % lang)

        translation.activate(lang)
        request.LANGUAGE_CODE = lang
        request.session[settings.LANGUAGE_COOKIE_NAME] = lang
        return None

    @staticmethod
    def process_response(request, response):
        lang = getattr(request, 'LANGUAGE_CODE', None) \
               or request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME)\
               or settings.DEFAULT_LANGUAGE

        if not request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME) \
                or (lang and lang != request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME)):
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang, max_age=1000)
        return response
