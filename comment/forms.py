from django import forms
from products.widgets import CustomClearableFileInput
from .models import Event


class EventForm(forms.ModelForm):
    """A form to add events"""


    class Meta:

        model = Event

        fields = [
            'title',
            'abstract',
            'body',
            'image',
            'status',
            'topped',
        ]
    
    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput,
    )