from pages.utils import get_flat_page
from snippets.views import BaseTemplateView, LangViewMixin


class Error404View(BaseTemplateView):

    template_name = 'errors/404.html'


class FlatpageView(LangViewMixin, BaseTemplateView):
    """Простые страницы"""

    template_name = 'pages/flatpage.html'

    def get_context_data(self, **kwargs):
        context = super(FlatpageView, self).get_context_data(**kwargs)
        context.update({
            'page': get_flat_page(kwargs.get('slug'))
        })
        return context
