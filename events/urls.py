
from django.urls import path
from .views import EventListView, EventDetailView, register_for_event, user_dashboard, CustomLoginView, CustomLogoutView, CustomRegistrationView
from .views import EventListAPIView, EventDetailAPIView, RegistrationCreateAPIView, UserRegistrationsAPIView


urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('event/<int:event_id>/register/', register_for_event, name='register_for_event'),
    path('dashboard/', user_dashboard, name='user_dashboard'),

    # Authentication URLs
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', CustomRegistrationView.as_view(), name='register'),

    # API URLs
    path('api/events/', EventListAPIView.as_view(), name='event-list-api'),
    path('api/events/<int:pk>/', EventDetailAPIView.as_view(), name='event-detail-api'),
    path('api/register/', RegistrationCreateAPIView.as_view(), name='register-api'),
    path('api/user-registrations/', UserRegistrationsAPIView.as_view(), name='user-registrations-api'),
]