from django.urls import path

from services import views


app_name = 'services'

urlpatterns = (
    path(
        'services/',
        views.ServicesView.as_view(),
        name='services'
    ),
    path(
        '<str:lang>/services/',
        views.ServicesView.as_view(),
        name='services_lang'
    ),
    path(
        'services/<slug:slug>/',
        views.ServiceView.as_view(),
        name='service'
    ),
    path(
        '<str:lang>/services/<slug:slug>/',
        views.ServiceView.as_view(),
        name='service_lang'
    )
)
