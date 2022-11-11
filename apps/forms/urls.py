from django.urls import path

from forms import views


app_name = 'forms'

urlpatterns = (
    path(
        'feedback/',
        views.FeedbackView.as_view(),
        name='feedback'
    ),
    path(
        '<str:lang>/feedback/',
        views.FeedbackView.as_view(),
        name='feedback_lang'
    ),
    path(
        'order/',
        views.OrderView.as_view(),
        name='order'
    ),
    path(
        '<str:lang>/order/',
        views.OrderView.as_view(),
        name='order_lang'
    ),
    path(
        'subscribe/',
        views.SubscribeView.as_view(),
        name='subscribe'
    ),
    path(
        '<str:lang>/subscribe/',
        views.SubscribeView.as_view(),
        name='subscribe_lang'
    )
)
