from django.urls import path

from .views import (
    EventDetailView,
    EventsListView,
    EventCreateView,
)

app_name = 'api'

urlpatterns = [
    path('events/', EventsListView.as_view()),
    path('events/<int:pk>', EventDetailView.as_view()),
    path('events/create-event', EventCreateView.as_view()),
]

