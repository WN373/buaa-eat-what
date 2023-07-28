from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Create your models here.
class FoodInfo(models.Model):
    id = models.AutoField(primary_key=True)
    food_name = models.CharField(max_length=128, verbose_name='菜品名', unique=True)
    price = models.CharField(max_length=64, verbose_name='价格')
    tags = TaggableManager(blank=True, verbose_name='标签')
    rating = models.FloatField(verbose_name='评分', default=0.0)
    stars = models.IntegerField(verbose_name='收藏量', default=0)
    purchases = models.IntegerField(verbose_name='购买量', default=0)
    photo_url = models.CharField(max_length=256, verbose_name='图片地址', default='')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')


class FoodFavor(models.Model):
    id = models.AutoField(primary_key=True)
    food = models.ForeignKey(FoodInfo, on_delete=models.CASCADE, verbose_name='菜品')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    created = models.DateTimeField(auto_now_add=True, verbose_name='收藏时间')


class TagFavor(models.Model):
    id = models.AutoField(primary_key=True)
    food = models.ForeignKey(FoodInfo, on_delete=models.CASCADE, verbose_name='菜品')
    tag = models.CharField(max_length=128, verbose_name='单标签')
    created = models.DateTimeField(auto_now_add=True, verbose_name='收藏时间')


class FoodPurchase(models.Model):
    id = models.AutoField(primary_key=True)
    food = models.ForeignKey(FoodInfo, on_delete=models.CASCADE, verbose_name='菜品')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    rating = models.IntegerField(verbose_name='评分', default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='购买时间')


class FoodComments(models.Model):
    id = models.AutoField(primary_key=True)
    food = models.ForeignKey(FoodInfo, on_delete=models.CASCADE, verbose_name='菜品')
    replied = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='回复')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    comment = models.CharField(max_length=256, verbose_name='评论内容')
    created = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    
    
