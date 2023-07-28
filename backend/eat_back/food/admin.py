from django.contrib import admin
from .models import FoodInfo, FoodComments, FoodPurchase

# Register your models here.
admin.site.register(FoodInfo)
admin.site.register(FoodComments)
admin.site.register(FoodPurchase)