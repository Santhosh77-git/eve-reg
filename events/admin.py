from django.contrib import admin
from .models import Event, Registration,Team


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "date", "capacity")
    search_fields = ("title", "location")
    list_filter = ("date",)

admin.site.register(Team)
