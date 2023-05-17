from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import EventForm


def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_calendar/event_list.html', {'events': events})


def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'event_calendar/event_detail.html', {'event': event})


def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_calendar:event-list')
    else:
        form = EventForm()
    return render(request, 'event_calendar/event_create.html', {'form': form})


def event_update(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_calendar:event-detail', id=id)
    else:
        form = EventForm(instance=event)
    return render(request, 'event_calendar/event_update.html', {'form': form, 'event': event})


def event_delete(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        event.delete()
        return redirect('event_calendar:event-list')
    return render(request, 'event_calendar/event_delete.html', {'event': event})
