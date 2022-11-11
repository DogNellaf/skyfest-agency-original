from django.urls import path

from contacts import views


app_name = 'contacts'

urlpatterns = (
    path(
        'contacts/',
        views.ContactsView.as_view(),
        name='contacts'
    ),
    path(
        '<str:lang>/contacts/',
        views.ContactsView.as_view(),
        name='contacts_lang'
    )
)
