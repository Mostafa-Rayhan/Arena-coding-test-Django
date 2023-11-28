
from django.urls import path
from .views import EventListView, EventDetailView, register_for_event, user_dashboard

urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),
    path('<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('<int:event_id>/register/', register_for_event, name='register_for_event'),
    path('dashboard/', user_dashboard, name='user_dashboard'),
]
