from django.urls import path, include
from main.views import show_main, create_item, register, login_user, logout_user, delete_item, increment_item, decrement_item, get_item_json, add_item_ajax, remove_item_ajax


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
    path('get-item/', get_item_json, name='get_item'),
    path('create-item-ajax/', add_item_ajax, name='add_item_ajax'),
    path('remove-item-ajax/', remove_item_ajax, name='remove_item_ajax')
]
