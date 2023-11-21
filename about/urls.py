from django.urls import path, include
from about.views import show_main

app_name = 'about'

urlpatterns = [
    path('', show_main, name='show_main'),
]