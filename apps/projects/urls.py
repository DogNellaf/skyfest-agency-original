from django.urls import path

from projects import views


app_name = 'projects'

urlpatterns = (
    path(
        'projects/',
        views.ProjectsView.as_view(),
        name='projects'
    ),
    path(
        '<str:lang>/projects/',
        views.ProjectsView.as_view(),
        name='projects_lang'
    ),
    path(
        'projects/<slug:slug>/',
        views.ProjectView.as_view(),
        name='project'
    ),
    path(
        '<str:lang>/projects/<slug:slug>/',
        views.ProjectView.as_view(),
        name='project_lang'
    )
)
