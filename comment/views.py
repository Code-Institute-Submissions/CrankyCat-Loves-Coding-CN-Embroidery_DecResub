from django.shortcuts import render, redirect, reverse, get_object_or_404
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


class DraftEventView(ListView):
    """a view for loading all draft events for the shop"""

    template_name = "comment/draft_events.html"
    context_object_name = "event_list"
    paginate_by = 3

    def get_queryset(self):
        event_list = Event.objects.filter(status='draft')

        for event in event_list:
            event.body = markdown2.markdown(event.body,)
        return event_list


@login_required
def add_event(request):
    """A from to add new events"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, Permission denied.')
        return redirect(reverse('home'))

    # allow template to pass in an empty form
    event_form = EventForm()

    # then save the form if method is post and form is valid
    if request.method == 'POST':
        event_form = EventForm(request.POST)

        if event_form.is_valid():
            event_form.save()
            messages.success(request, 'Successfully added event!')
            return redirect('add_event')
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

    return render(request, 'comment/add_event.html', context)


@login_required
def edit_event(request, event_id):
    """edit store events"""

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, Permission denied.')
        return redirect(reverse('home'))

    event = get_object_or_404(Event, pk=event_id)
    
    if request.method == 'POST':
        event_form = EventForm(request.POST, request.FILES, instance=event)
        if event_form.is_valid():
            event_form.save()
            messages.success(
                request,
                f'Successfully updated {event.title}!'
            )
            if event.status == 'published':
                return redirect(
                    reverse('events')
                )
            return redirect(
                reverse('draft_events')
            )
        messages.error(
            request,
            f'Failded to update {event.title}! Please try again later.'
        )
    else:
        event_form = EventForm(instance=event)
        messages.info(
            request,
            f'You are editing {event.title}'
        )

    context = {
        'form': event_form,
        'event': event,
    }

    return render(request, 'comment/edit_event.html', context)



@login_required
def delete_event(request, event_id):
    """delete store events"""

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, Permission denied.')
        return redirect(reverse('home'))

    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    messages.success(
        request,
        f'{event.status} event {event.title} deleted!'
    )
    return redirect(reverse('events',))
