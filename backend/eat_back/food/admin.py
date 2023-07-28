from django.contrib import admin
from .models import FoodInfo, FoodComments, FoodFavor, FoodPurchase, TagFavor

# Register your models here.
admin.site.register(FoodInfo)
admin.site.register(FoodComments)
admin.site.register(FoodFavor)
admin.site.register(FoodPurchase)
admin.site.register(TagFavor)
