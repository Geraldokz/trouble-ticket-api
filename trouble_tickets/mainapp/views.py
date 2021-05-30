from django.shortcuts import render
from django.views.generic import ListView

from .models import Event


class MainPage(ListView):
    model = Event
    template_name = 'mainapp/index.html'
    context_object_name = 'events'
