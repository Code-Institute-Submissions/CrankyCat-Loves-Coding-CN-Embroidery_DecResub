from django.contrib import admin
from comment.models import Event
from django_summernote.admin import SummernoteModelAdmin

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