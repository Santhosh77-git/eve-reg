from rest_framework import serializers
from .models import Event, Registration
from django.contrib.auth.models import User


class EventSerializer(serializers.ModelSerializer):
    registered_teams_count = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = "__all__"

    def get_registered_teams_count(self, obj):
        return obj.registration_set.count()

class RegistrationSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source='team.team_name', read_only=True)
    event_title = serializers.CharField(source='event.title', read_only=True)
    class Meta:
        model = Registration
        fields = ['id', 'event','event_title',
            'team_name', 'registered_at']
        read_only_fields = ['id', 'registered_at']
