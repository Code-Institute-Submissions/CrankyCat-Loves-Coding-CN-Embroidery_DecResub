import markdown2
from comment.models import Event
from django.views.generic import ListView



class EventView(ListView):
    template_name = "comment/event.html"
    context_object_name = "event_list"

    def get_queryset(self):
        event_list = Event.objects.filter(status='p') 

        for event in event_list:
            event.body = markdown2.markdown(event.body, )  
        return event_list 

    