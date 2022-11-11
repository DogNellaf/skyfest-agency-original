from django.shortcuts import get_object_or_404

from . import models
from snippets.choices import StatusChoices
from snippets.views import BaseTemplateView, LangViewMixin


class EventsView(LangViewMixin, BaseTemplateView):
    """Страница мероприятий"""

    template_name = 'events/events.html'

    def get_context_data(self, **kwargs):
        kwargs = super(EventsView, self).get_context_data(**kwargs)
        page = models.EventsPage.get_solo()
        events = models.Event.objects.published()
        kwargs.update(
            page=page,
            events=events
        )
        return kwargs


class EventView(LangViewMixin, BaseTemplateView):
    """Страница мероприятия"""

    template_name = 'events/event.html'

    def get_context_data(self, **kwargs):
        kwargs = super(EventView, self).get_context_data(**kwargs)
        list_page = models.EventsPage.get_solo()
        event = get_object_or_404(
            models.Event.objects.published(), slug=kwargs['slug']
        )
        event.show_subscribe = list_page.show_subscribe
        event.subscribe_block = list_page.subscribe_block

        gallery_photos = []
        if (
            event.gallery_id
            and event.gallery.status == StatusChoices.PUBLIC.value
        ):
            gallery_photos = event.gallery.photos.published()

        kwargs.update(
            gallery_photos=gallery_photos,
            page=event,
            indicators=event.indicators.published(),
            list_page=list_page,
            section_icons=event.section_icons.published()
        )
        return kwargs
