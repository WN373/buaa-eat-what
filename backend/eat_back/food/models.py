from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class FoodInfo(models.Model):
    foodName = models.CharField(max_length=128, verbose_name='菜品名')
    parentName = models.CharField(max_length=128, unique=True, verbose_name='餐厅名')
    price = models.FloatField(verbose_name='价格')
    stars = models.IntegerField(verbose_name='收藏量')
    purchases = models.IntegerField(verbose_name='购买量')


class FoodComments(models.Model):
    food = models.ForeignKey(FoodInfo, on_delete=models.CASCADE, verbose_name='菜品')
    replied = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='回复')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    comment = models.CharField(verbose_name='评论内容')
    created = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
