from django.contrib import admin
from comment.models import Event

@admin.register(Event)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'abstract',
        'created_time',
        'status',
        'views',
        'likes',
    )