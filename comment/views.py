"""view for store events and comments"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import markdown2

from .models import Event, Comment
from .forms import EventForm, CommentForm


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


def event_details_view(request, event_id):
    """A view for render single event details"""

    event_details = get_object_or_404(Event, pk=event_id)
    comments = Comment.objects.filter(event=event_id)

    context = {
        'event_details': event_details,
        'comments': comments
    }

    return render(request, 'comment/event_details.html', context)


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


@login_required
def post_comment(request, event_id):
    """comments for events"""

    if not request.user.is_authenticated:
        messages.error(request, 'Please login to leave a comment.')
        return redirect(reverse('events'))

    event = get_object_or_404(Event, pk=event_id)

    if request.method == 'POST':

        comment_form = CommentForm(request.POST)
        event_details = get_object_or_404(Event, pk=event_id)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.event = event
            new_comment.user = request.user
            new_comment.save()
            messages.success(
                request,
                'Comment added Successfully!'
            )
            return redirect(
                reverse('event_details', args=[event_details.id])
            )
        messages.error(
            request,
            'Failded to leave a comment! Please try again later.'
        )
    else:
        comment_form = CommentForm(instance=event)
        messages.info(
            request,
            'You are leaving a comment!'
        )
