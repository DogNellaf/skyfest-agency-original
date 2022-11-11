from django.urls import path

from about import views


app_name = 'about'

urlpatterns = (
    path(
        'about/',
        views.AboutView.as_view(),
        name='about'
    ),
    path(
        '<str:lang>/about/',
        views.AboutView.as_view(),
        name='about_lang'
    )
)
