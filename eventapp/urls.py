from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home" ),
    path("register/", views.register, name="register"),
    path('events/', views.event_list, name='event_list'),
    path('events/create/', views.create_event, name='create_event'),
]