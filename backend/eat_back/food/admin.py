from django.contrib import admin

from food.models import FoodInfo, UsrInfo

# Register your models here.
admin.site.register(FoodInfo)
admin.site.register(UsrInfo)