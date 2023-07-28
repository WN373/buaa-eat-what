from django.contrib import admin
from django.urls import path,include
from .views import *

# food/
urlpatterns = [
    path('comment/', get_comment_list, name='get_comment_list'),
    path('commenton/', post_new_comment, name='post_new_comment'),
    path('createfood/', create_food, name='create_food'),
    path('getfoodbyname/', get_food_by_name, name='get_food_by_name'),
    path('favorfood/', create_food_favor, name='create_food_favor'),
    path('unfavorfood/', delete_food_favor, name='delete_food_favor'),
]