from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventView.as_view(), name='events'),
    path('add_event/', views.add_event, name='add_event'),
    path('edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('draft_events/', views.DraftEventView.as_view(), name='draft_events'),
    path(
        'delete/<int:event_id>/',
        views.delete_event,
        name='delete_event'
    ),
    # path('', views.comment_details, name='comments_details'),
    path(
        'post-comment/<int:event_id>/',
        views.post_comment,
        name='post_comment'
    ),
]
