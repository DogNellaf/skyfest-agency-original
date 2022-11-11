from django.urls import path

from . import views


app_name = 'events'

urlpatterns = (
    path(
        'events/',
        views.EventsView.as_view(),
        name='events'
    ),
    path(
        '<str:lang>/events/',
        views.EventsView.as_view(),
        name='events_lang'
    ),
    path(
        'events/<slug:slug>/',
        views.EventView.as_view(),
        name='event'
    ),
    path(
        '<str:lang>/events/<slug:slug>/',
        views.EventView.as_view(),
        name='event_lang'
    )
)
