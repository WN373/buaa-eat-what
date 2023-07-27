from django.shortcuts import render

# Create your views here.
from .models import *
from django.http import JsonResponse

def get_comment_list(request):
    if request.method == 'GET':
        food_name = request.GET.get('food_name')
        food = FoodInfo.objects.filter(foodName=food_name)
        comments = FoodComments.objects.filter(food=food).order_by('-created')
        return JsonResponse({'code': 200, 'msg': '获取评论成功', 'data': comments})
    else:
        return JsonResponse({'code': 400, 'msg': '请求方式错误'})
