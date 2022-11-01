from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import markdown2

from .models import Event
from .forms import EventForm


class EventView(ListView):
    """a view for loading all events for the shop"""

    template_name = "comment/event.html"
    context_object_name = "event_list"
    paginate_by = 3

    def get_queryset(self):
        event_list = Event.objects.filter(status='published')

        for event in event_list:
            event.body = markdown2.markdown(event.body,)
        return event_list


@login_required
def add_event(request):
    """A from to add new events"""

    # allow template to pass in an empty form
    event_form = EventForm()

    # then save the form if method is post and form is valid
    if request.method == 'POST':
        event_form = EventForm(request.POST)

        if event_form.is_valid():
            event_form.save()
            messages.success(request, 'Successfully added event!')
            return redirect('addevent')
        else:
            messages.error(
                request,
                (
                    'Failed to add event. '
                    'Please try later.'
                )
            )

    context = {
        'form': event_form,
    }

    return render(request, 'comment/addevent.html', context)


# class AddEventView(ListView):
#     """A view to render all draft events """

#     template_name = "comment/addevent.html"
#     context_object_name = "event_list"
#     paginate_by = 3
#     # def get(self, request, *args, **kwargs):
#     #     event_form = EventForm()
#     #     return render(request, 'comment/addevent.html', {"form":event_form})

#     def get_queryset(self):
#         # render all draft events
#         event_list = Event.objects.filter(status='draft')

#         for event in event_list:
#             event.body = markdown2.markdown(event.body,)
#         return event_list


#     def addeventform(self, request, *args, **kwargs):
#         """A from to add new events"""
#         # allow template to pass in an empty form
#         event_form = EventForm()

#         # then save the form if method is post and form is valid
#         if request.method == 'POST':
#             event_form = EventForm(request.POST)

#             if event_form.is_valid():
#                 event_form.save()
#                 return redirect('addevent')
        
#         # context = {
#         #     'event_form': event_form,
#         # }

#         # return render(request, 'comment/addevent.html', context)
#         return render(request, 'comment/addevent.html', {"form":event_form})
#         # {"form": form}
