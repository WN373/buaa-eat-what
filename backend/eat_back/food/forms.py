from django import forms
from .models import FoodInfo, FoodPurchase


class FoodInfoForm(forms.ModelForm):
    class Meta:
        model = FoodInfo
        fields = ['food_name', 'price', 'tags', 'photo_url']
        required = {'photo_url': False,
                    'tags': False,
                    'price': False,
                    }
        labels = {
            'food_name': '菜品名',
            'price': '价格',
            'tags': '标签',
            'photo_url': '图片地址'
        }

