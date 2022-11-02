from django import forms
from django_summernote.fields import SummernoteTextField
from .models import Event


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
            'topped',
        ]
