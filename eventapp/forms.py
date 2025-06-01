from django import forms
from .models import Event
from django.forms.widgets import SelectDateWidget

class EventForm(forms.ModelForm):
    date = forms.DateField(widget=SelectDateWidget)
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location', 'price', 'is_vip_available', 'category']
