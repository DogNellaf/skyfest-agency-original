from django.urls import path

from blog import views


app_name = 'blog'

urlpatterns = (
    path(
        'blog/',
        views.BlogView.as_view(),
        name='blog'
    ),
    path(
        '<str:lang>/blog/',
        views.BlogView.as_view(),
        name='blog_lang'
    ),
    path(
        'blog/<slug:slug>/',
        views.ArticleView.as_view(),
        name='article'
    ),
    path(
        '<str:lang>/blog/<slug:slug>/',
        views.ArticleView.as_view(),
        name='article_lang'
    )
)
