from sys import maxunicode

from django.db import models
from django.contrib.auth.models import User

LOCATION_CHOICES = [
    ('hall_a', 'Hall A'),
    ('hall_b', 'Hall B'),
    ('johns_house', "John's House"),
]
CATEGORY_CHOICES = [
    ('music', 'Music'),
    ('sports', 'Sports'),
    ('tech', 'Technology'),
    ('other', 'Other')
]
class EventCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Event Model
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_vip_available = models.BooleanField(default=False)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(choices=CATEGORY_CHOICES, default='music', max_length=100)

    def __str__(self):
        return self.title

# Registration Model
class Registration(models.Model):
    TICKET_TYPES = (
        ('general', 'General Admission'),
        ('vip', 'VIP'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=10, choices=TICKET_TYPES)
    is_paid = models.BooleanField(default=False)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"
