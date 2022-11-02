from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventView.as_view(), name='events'),
    path('addevent/', views.add_event, name='addevent'),
    path('draftevents/', views.DraftEventView.as_view(), name='draftevents'),
    path(
        'delete/<int:event_id>/',
        views.delete_event,
        name='delete_event'
    ),
]
