from django import forms
from .models import FoodInfo


class FoodInfoForm(forms.ModelForm):
    class Meta:
        model = FoodInfo
        fields = ['food_name', 'price', 'tags']
        labels = {
            'food_name': '菜品名',
            'price': '价格',
            'tags': '标签'
        }