from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from comment.models import Event, Comment

@admin.register(Event)
class PostAdmin(SummernoteModelAdmin):

    list_display = (
        'title',
        'abstract',
        'created_time',
        'status',
        'views',
        'likes',
    )

    summernote_fields = ('body')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'body', 'created_time')