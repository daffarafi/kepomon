from django.urls import path, include
from main.views import show_main, create_item

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('about/', include('about.urls')),
    path('create-item', create_item, name='create_item'),

]