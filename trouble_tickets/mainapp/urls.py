from django.urls import path

from .views import MainPage

app_name = 'mainapp'

urlpatterns = [
    path('', MainPage.as_view())
]
