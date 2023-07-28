from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Create your models here.
class FoodInfo(models.Model):
    id = models.AutoField(primary_key=True)
    food_name = models.CharField(max_length=128, verbose_name='菜品名', unique=True)
    price = models.CharField(max_length=64, verbose_name='价格', default='0.0')
    tags = TaggableManager(blank=True, verbose_name='标签')
    comments = models.IntegerField(verbose_name='评论数', default=0)
    rating = models.FloatField(verbose_name='评分', default=0.0)
    stars = models.IntegerField(verbose_name='收藏量', default=0)
    purchases = models.IntegerField(verbose_name='购买量', default=0)
    photo_url = models.CharField(max_length=256, verbose_name='图片地址', default='', blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

class RegionInfo(models.Model):
    id = models.AutoField(primary_key=True)
    region_name = models.CharField(max_length=128, verbose_name='地区名', unique=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

class CounterInfo(models.Model):
    id = models.AutoField(primary_key=True)
    counter_name = models.CharField(max_length=128, verbose_name='柜台名')
    region = models.ForeignKey(RegionInfo, on_delete=models.CASCADE, verbose_name='地区')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

class FoodPurchase(models.Model):
    id = models.AutoField(primary_key=True)
    food = models.ForeignKey(FoodInfo, on_delete=models.CASCADE, verbose_name='菜品')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    rating = models.IntegerField(verbose_name='评分', default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='购买时间')

class FoodFavor(models.Model):
    id = models.AutoField(primary_key=True)
    food = models.ForeignKey(FoodInfo, on_delete=models.CASCADE, verbose_name='菜品')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    created = models.DateTimeField(auto_now_add=True, verbose_name='收藏时间')

class RegionFavor(models.Model):
    id = models.AutoField(primary_key=True)
    region = models.ForeignKey(RegionInfo, on_delete=models.CASCADE, verbose_name='地区')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    created = models.DateTimeField(auto_now_add=True, verbose_name='收藏时间')

class CounterFavor(models.Model):
    id = models.AutoField(primary_key=True)
    counter = models.ForeignKey(CounterInfo, on_delete=models.CASCADE, verbose_name='柜台')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    created = models.DateTimeField(auto_now_add=True, verbose_name='收藏时间')

class FoodComments(models.Model):
    id = models.AutoField(primary_key=True)
    food = models.ForeignKey(FoodInfo, on_delete=models.CASCADE, verbose_name='菜品')
    replied = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='回复')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    comment = models.CharField(max_length=256, verbose_name='评论内容')
    is_anonymous = models.BooleanField(default=False, verbose_name='是否匿名', blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
