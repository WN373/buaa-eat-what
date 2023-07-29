from django.contrib import admin
from django.urls import path,include
from .views import *

# food/
urlpatterns = [
    path('buyfood/', buy_food, name='buy_food'),
    # food comments
    path('comment/', get_comment_list, name='get_comment_list'),
    path('commenton/', post_new_comment, name='post_new_comment'),
    # food info
    path('createfood/', create_food, name='create_food'),
    path('getfoodbyname/', get_food_by_name, name='get_food_by_name'),
    path('gettopfood/', get_top_food, name='get_top_food'),
    path('getpurchasehistory/', get_purchase_history, name='get_purchase_history'),
    path('deletepurchasehistory/', delete_purchase_history, name='delete_purchase_history'),
    path('changepurchasehistory/', change_purchase_history, name='change_purchase_history'),
    # food favor
    path('favorfood/', create_food_favor, name='create_food_favor'),
    path('unfavorfood/', delete_food_favor, name='delete_food_favor'),
    path('getfoodfavor/', get_food_favor, name='get_food_favor'),
    # region & counter favor
    path('createregion/', create_region, name='create_region'),
    path('getregions/', get_regions, name='get_region'),
    path('createcounter/', create_counter, name='create_counter'),
    path('getcounters/', get_counters_by_region, name='get_counter'),
    path('favorregion/', modify_region_favor, name='modify_region_favor'),
    path('favorcounter/', modify_counter_favor, name='modify_counter_favor'),
    path('getregionfavor/', get_region_favor, name='get_region_favor'),
    path('getcounterfavor/', get_counter_favor, name='get_counter_favor'),
]