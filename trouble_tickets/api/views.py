from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .filters import EventFilter
from .serializers import EventSerializer
from .services import EventPagination

from mainapp.models import Event


class EventsListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = EventFilter
    pagination_class = EventPagination


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventCreateView(generics.CreateAPIView):
    serializer_class = EventSerializer
