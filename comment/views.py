"""view for store events and comments"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView
from django.core.paginator import Paginator
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
    context_object_name = "draft_events"
    paginate_by = 3

    def get_queryset(self):
        draft_events = Event.objects.filter(status='draft')

        for event in draft_events:
            event.body = markdown2.markdown(event.body,)
        return draft_events


def event_details_view(request, event_id):
    """A view for render single event details and comments"""

    event_details = get_object_or_404(Event, pk=event_id)
    comments = Comment.objects.filter(event=event_id).order_by("-created_time")

    # total of views
    event_details.views += 1
    event_details.save(update_fields=['views'])

    # set up pagination
    display = Paginator(comments, 5)
    page = request.GET.get('page')
    comment_list = display.get_page(page)

    context = {
        'event_details': event_details,
        'comments': comments,
        'comment_list': comment_list
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
            return redirect(request.META.get('HTTP_REFERER'))
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
    if event.status == 'published':
        return redirect(
            reverse('events')
        )
    return redirect(
        reverse('draft_events')
    )


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


@login_required
def delete_comment(request, comment_id):
    """ Delete a comment, only apply to a superuser """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, Permission denied.')
        return redirect(reverse('events'))

    # get the comment by the id
    comment = get_object_or_404(Comment, pk=comment_id)

    # get the page user currently at
    event_id = comment.event.id

    # delete the comment
    comment.delete()

    # send user a message
    messages.success(request, f'Comment {comment.body} deleted.')

    # redirect to the page
    return redirect(reverse('event_details', args=[event_id]))
