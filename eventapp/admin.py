from django.contrib import admin

# Register your models here.
from .models import Event, EventCategory, Registration

admin.site.register(Event)
admin.site.register(EventCategory)
admin.site.register(Registration)