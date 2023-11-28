
from django.urls import path
from .views import EventListAPIView, EventDetailAPIView, RegistrationCreateAPIView, UserRegistrationsAPIView

urlpatterns = [
    path('events/', EventListAPIView.as_view(), name='event-list-api'),
    path('events/<int:pk>/', EventDetailAPIView.as_view(), name='event-detail-api'),
    path('register/', RegistrationCreateAPIView.as_view(), name='register-api'),
    path('user/registrations/', UserRegistrationsAPIView.as_view(), name='user-registrations-api'),
]
