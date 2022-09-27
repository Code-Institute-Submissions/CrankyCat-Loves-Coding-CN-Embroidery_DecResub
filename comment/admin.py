from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    '''register Comment app to admin site'''
    list_display = ['like']


admin.site.register(Comment, CommentAdmin)
