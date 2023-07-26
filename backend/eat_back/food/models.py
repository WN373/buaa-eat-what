from django.db import models

# Create your models here.
class FoodInfo(models.Model):
    foodName = models.CharField(max_length=128, verbose_name='菜品名')
    parentName = models.CharField(max_length=128, unique=True, verbose_name='餐厅名')
    price = models.FloatField(verbose_name='价格')
    stars = models.IntegerField(verbose_name='收藏量')
    purchases = models.IntegerField(verbose_name='购买量')
    
    
class UsrInfo(models.Model):
    usrName = models.CharField(max_length=128, verbose_name='用户名')
    usrGender = models.BooleanField(verbose_name='性别')