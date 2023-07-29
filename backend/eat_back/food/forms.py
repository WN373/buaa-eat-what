from django import forms
from .models import FoodInfo, FoodPurchase, RegionInfo, CounterInfo


class FoodInfoForm(forms.ModelForm):
    region_name = forms.CharField(max_length=128, label='地区名')
    counter_name = forms.CharField(max_length=128, label='柜台名')

    class Meta:
        # model = FoodInfo
        fields = ['food_name', 'price', 'tags', 'photo_url', 'region_name', 'counter_name']
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

    def save(self):
        data = self.cleaned_data
        region = RegionInfo.objects.get(region_name=data['region_name'])
        counter = CounterInfo.objects.get(counter_name=data['counter_name'], region=region)
        food = FoodInfo.objects.create(food_name=data['food_name'], price=data['price'], region=region,
                                       counter=counter, photo_url=data['photo_url'], tags=data['tags'])
        food.save()