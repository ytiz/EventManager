from django.shortcuts import HttpResponse, render, redirect

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Event, EventCategory
from django.contrib.auth.decorators import login_required
from .forms import EventForm


def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in the user automatically
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})
def event_list(request):
    events = Event.objects.all()
    categories = EventCategory.objects.all()

    # Filters
    category = request.GET.get('category')
    search = request.GET.get('search')
    if category:
        events = events.filter(category__id=category)
    if search:
        events = events.filter(title__icontains=search)

    return render(request, 'events/event_list.html', {
        'events': events,
        'categories': categories,
    })

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})
