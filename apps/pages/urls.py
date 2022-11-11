from django.urls import path

from pages import views


app_name = 'pages'

urlpatterns = (
    path(
        '<slug:slug>/',
        views.FlatpageView.as_view(),
        name='flatpage'
    ),
    path(
        '<str:lang>/<slug:slug>/',
        views.FlatpageView.as_view(),
        name='flatpage_lang'
    )
)
