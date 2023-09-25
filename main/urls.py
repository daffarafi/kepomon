from django.urls import path, include
from main.views import show_main, create_item, register, login_user, logout_user, delete_item, increment_item, decrement_item


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('about/', include('about.urls')),
    path('create-item', create_item, name='create_item'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete-item/<int:id>', delete_item, name="delete-item"),
    path('increment-item/<int:id>', increment_item, name="increment-item"),
    path('decrement-item/<int:id>', decrement_item, name="decrement-item"),
]