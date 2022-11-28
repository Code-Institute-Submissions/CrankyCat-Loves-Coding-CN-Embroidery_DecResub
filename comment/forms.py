from django import forms
from django_summernote.fields import SummernoteTextField
from .models import Event, Comment


class EventForm(forms.ModelForm):
    """A form to add events"""
    
    body = SummernoteTextField()

    class Meta:
        
        model = Event
        
        fields = [
            'title',
            'abstract',
            'body',
            'status',
        ]


class CommentForm(forms.ModelForm):
    """A form to add comments"""

    class Meta:
        
        model = Comment
        
        fields = [
            'body',
        ]
