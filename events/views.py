
from django.shortcuts import render, redirect
from django.views import generic
from .models import Event, Registration
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Event, Registration
from .serializers import EventSerializer, RegistrationSerializer

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

class EventListView(generic.ListView):
    model = Event
    template_name = 'event_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Event.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
        return Event.objects.all()

class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'event_detail.html'

@login_required
def register_for_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    
    if request.method == 'POST':
        if event.available_slots > 0:
            Registration.objects.create(user=request.user, event=event)
            event.available_slots -= 1
            event.save()
            messages.success(request, 'You have successfully registered for the event.')
        else:
            messages.error(request, 'Sorry, no available slots for this event.')
        return redirect('event_detail', pk=event_id)

@login_required
def user_dashboard(request):
    registrations = Registration.objects.filter(user=request.user)
    return render(request, 'user_dashboard.html', {'registrations': registrations})



class CustomLoginView(LoginView):
    template_name = 'login.html'

class CustomLogoutView(LogoutView):
    next_page = 'event_list'

class CustomRegistrationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')



class EventListAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetailAPIView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class RegistrationCreateAPIView(generics.CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]

class UserRegistrationsAPIView(generics.ListAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Registration.objects.filter(user=self.request.user)
