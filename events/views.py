from rest_framework import generics, permissions, viewsets
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.exceptions import ValidationError
from django.db import IntegrityError

from .models import Event, Registration
from .serializers import EventSerializer, RegistrationSerializer


# ===============================
# EVENT VIEWS
# ===============================

# GET all events + POST create event
class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


# GET single event detail
class EventDetailView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


# Admin control for events
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [AllowAny()]


# ===============================
# REGISTRATION VIEWS
# ===============================

class RegistrationListCreateView(generics.ListCreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]

    # Show only logged-in team's registrations
    def get_queryset(self):
        return Registration.objects.filter(
            team=self.request.user.team
        )

    # Register for event
    def perform_create(self, serializer):
        event = serializer.validated_data['event']
        team = self.request.user.team

        # 🔥 Duplicate check
        if Registration.objects.filter(team=team, event=event).exists():
            raise ValidationError(
                {"error": "You are already registered for this event."}
            )

        # 🔥 Capacity check
        if Registration.objects.filter(event=event).count() >= event.capacity:
            raise ValidationError(
                {"error": "This event is full."}
            )

        serializer.save(team=team)


# View only my registrations
class MyRegistrationsView(generics.ListAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Registration.objects.filter(
            team=self.request.user.team
        )


# Cancel registration
class CancelRegistrationView(generics.DestroyAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Registration.objects.filter(
            team=self.request.user.team
        )