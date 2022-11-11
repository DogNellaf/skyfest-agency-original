from about import models
from snippets.views import BaseTemplateView, LangViewMixin


class AboutView(LangViewMixin, BaseTemplateView):
    """Страница о компании"""

    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        kwargs = super(AboutView, self).get_context_data(**kwargs)
        page = models.AboutPage.get_solo()
        kwargs.update(
            page=page,
            services=[x.service for x in page.services.published().select_related('service')],
            team=page.employees.published()
        )
        return kwargs
