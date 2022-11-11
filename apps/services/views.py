from django.shortcuts import get_object_or_404

from services import models
from snippets.views import BaseTemplateView, LangViewMixin


class ServicesView(LangViewMixin, BaseTemplateView):
    """Страница услуг"""

    template_name = 'services/services.html'

    def get_context_data(self, **kwargs):
        kwargs = super(ServicesView, self).get_context_data(**kwargs)
        page = models.ServicesPage.get_solo()
        services = models.Service.objects.published()
        kwargs.update(
            page=page,
            services=services
        )
        return kwargs


class ServiceView(LangViewMixin, BaseTemplateView):
    """Страница услуги"""

    template_name = 'services/service.html'

    def get_context_data(self, **kwargs):
        kwargs = super(ServiceView, self).get_context_data(**kwargs)
        list_page = models.ServicesPage.get_solo()
        service = get_object_or_404(
            models.Service.objects.published(), slug=kwargs['slug']
        )
        services = list(models.Service.objects.published())
        projects = service.projects.published()
        service.show_subscribe = list_page.show_subscribe
        service.subscribe_block = list_page.subscribe_block

        previous_service, next_service = None, None
        for i, serv in enumerate(services):
            if serv.id == service.id:
                if i > 0:
                    previous_service = services[i - 1]

                if i + 1 < len(services):
                    next_service = services[i + 1]

        kwargs.update(
            page=service,
            list_page=list_page,
            next_service=next_service,
            previous_service=previous_service,
            projects=projects,
            services=services
        )
        return kwargs
