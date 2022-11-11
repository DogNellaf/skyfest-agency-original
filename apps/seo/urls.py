from django.conf.urls import url

from seo import views

app_name = 'seo'
urlpatterns = (
    url(r'^sitemap.xml$', views.SitemapView.as_view(), name='sitemap'),
    url(r'^robots.txt$', views.RobotsView.as_view(), name='robots'),
)
