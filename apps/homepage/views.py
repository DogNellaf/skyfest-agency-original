import math

from blog.models import Article
from homepage import models
from snippets.views import BaseTemplateView, LangViewMixin


class HomeView(LangViewMixin, BaseTemplateView):
    """Главная страница"""

    template_name = 'homepage/homepage.html'

    def get_context_data(self, **kwargs):
        kwargs = super(HomeView, self).get_context_data(**kwargs)
        page = models.HomePage.get_solo()
        projects = [x.project for x in page.projects.published().select_related('project')]
        if len(projects) < 3:
            base_projects = list(projects)
            for i in range(math.ceil(3.0 / len(projects))):
                projects.extend(list(base_projects))

        kwargs.update(
            articles=Article.objects.published().actual().filter(show_on_home=True)[:3],
            brands=[x.brand for x in page.brands.published().select_related('brand')],
            page=page,
            projects=projects,
            services=[x.service for x in page.services.published().select_related('service')]
        )
        return kwargs
