from django.urls import path
from . import views 
from rest_framework.routers import DefaultRouter
from .views import (
     EventListCreateView,
    EventDetailView,
    RegistrationListCreateView,
    MyRegistrationsView,
    CancelRegistrationView
)

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),

    path('registrations/', RegistrationListCreateView.as_view(), name='register-event'),
    path('my-registrations/', MyRegistrationsView.as_view(), name='my-registrations'),
    path('cancel-registration/<int:pk>/', CancelRegistrationView.as_view(), name='cancel-registration'),
]
router = DefaultRouter()
router.register(r'events', views.EventViewSet)

