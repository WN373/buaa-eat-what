from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(FoodInfo)
admin.site.register(FoodComments)
admin.site.register(FoodFavor)
admin.site.register(FoodPurchase)
admin.site.register(RegionInfo)
admin.site.register(RegionFavor)
admin.site.register(CounterInfo)
admin.site.register(CounterFavor)

