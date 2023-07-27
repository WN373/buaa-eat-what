from django.contrib import admin
from .models import FoodInfo, FoodComments

# Register your models here.
admin.site.register(FoodInfo)
admin.site.register(FoodComments)