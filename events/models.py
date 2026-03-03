from django.db import models
from django.contrib.auth.models import User

# ========================
# Event Model
# ========================
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date = models.DateTimeField()
    capacity = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# ========================
# Registration Model
# ========================
class Registration(models.Model):
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)

    registered_at = models.DateTimeField(auto_now_add=True)
    is_cancelled = models.BooleanField(default=False)

    
    def __str__(self):
         return f"{self.team.team_name} - {self.event.name}"
    class Meta:
        unique_together = ("team", "event")  # 🚨 prevents duplicate registration


class Team(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=100, unique=True)
    college_name = models.CharField(max_length=200)
    leader_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)

    def __str__(self):
        return self.team_name