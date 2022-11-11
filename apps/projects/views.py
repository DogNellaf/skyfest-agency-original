from django.shortcuts import get_object_or_404

from projects import models
from snippets.choices import StatusChoices
from snippets.views import BaseTemplateView, LangViewMixin


class ProjectsView(LangViewMixin, BaseTemplateView):
    """Страница проектов"""

    template_name = 'projects/projects.html'

    def get_context_data(self, **kwargs):
        kwargs = super(ProjectsView, self).get_context_data(**kwargs)
        page = models.ProjectsPage.get_solo()
        projects = models.Project.objects.published()
        kwargs.update(
            page=page,
            projects=projects
        )
        return kwargs


class ProjectView(LangViewMixin, BaseTemplateView):
    """Страница проекта"""

    template_name = 'projects/project.html'

    def get_context_data(self, **kwargs):
        kwargs = super(ProjectView, self).get_context_data(**kwargs)
        list_page = models.ProjectsPage.get_solo()
        project = get_object_or_404(
            models.Project.objects.published(), slug=kwargs['slug']
        )
        project.show_subscribe = list_page.show_subscribe
        project.subscribe_block = list_page.subscribe_block

        gallery_photos = []
        if project.gallery_id and project.gallery.status == StatusChoices.PUBLIC.value:
            gallery_photos = project.gallery.photos.published()

        kwargs.update(
            gallery_photos=gallery_photos,
            page=project,
            indicators=project.indicators.published(),
            list_page=list_page,
            section_icons=project.section_icons.published()
        )
        return kwargs
