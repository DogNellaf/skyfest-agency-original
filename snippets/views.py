from django.conf import settings
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView


class LangViewMixin(object):
    def dispatch(self, request, *args, **kwargs):
        match = request.resolver_match
        if kwargs.get('lang') == settings.LANGUAGE_CODE \
                and match.url_name.endswith('_lang'):
            new_kwargs = kwargs.copy()
            del new_kwargs['lang']
            new_name = match.url_name.replace("_lang", "")
            return HttpResponsePermanentRedirect(reverse(
                f'{match.namespace}:{new_name}',
                args=args,
                kwargs=new_kwargs
            ))
        return super(LangViewMixin, self).dispatch(request, *args, **kwargs)


class BaseTemplateView(TemplateView):
    """Базовый класс для представлений c шаблоном"""
    template_name = None
    template_engine = 'jinja2'
    content_type = 'text/html'

    def get_context_data(self, **kwargs):
        kwargs = super(BaseTemplateView, self).get_context_data(**kwargs)
        kwargs['request'] = kwargs['view'].request
        return kwargs

    def get_page(self, param='page'):
        """Получает номер страницы пагинации"""
        page = self.kwargs.get(param)
        try:
            page = int(page)
        except (ValueError, TypeError):
            page = 1

        if page < 1:
            page = 1

        return page


class BaseView(View):
    """Базовый класс для представлений"""
    pass
