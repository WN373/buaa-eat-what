from django import forms
from .models import FoodInfo, FoodPurchase, RegionInfo, CounterInfo
from taggit.models import Tag


class FoodInfoForm(forms.ModelForm):
    region_name = forms.CharField(max_length=128, label='地区名')
    counter_name = forms.CharField(max_length=128, label='柜台名')

    class Meta:
        model = FoodInfo
        fields = ['food_name', 'price', 'tags', 'photo_url', 'region_name', 'counter_name']
        required = {'photo_url': False,
                    'tags': False,
                    'price': False,
                    'region_name': False,
                    'counter_name': False
                    }
        labels = {
            'food_name': '菜品名',
            'price': '价格',
            'tags': '标签',
            'photo_url': '图片地址'
        }

    def save(self):
        data = self.cleaned_data
        if data['region_name'] == '':
            region = None
            counter = None
        else:
            region = RegionInfo.objects.get(region_name=data['region_name'])
            if data['counter_name'] == '':
                counter = None
            else:
                counter = CounterInfo.objects.get(counter_name=data['counter_name'], region=region)

        food = FoodInfo.objects.create(food_name=data['food_name'], price=data['price'], region=region,
                                       counter=counter, photo_url=data['photo_url'])
        food.save()
        food.tags.add(*data['tags'])
        food.save()
