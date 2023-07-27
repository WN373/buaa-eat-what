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


# post_new_comment
# format:
# {
#     'food_name': '事物名称',
#     'replied': '回复对象',
#     'comment': '评论内容',
#     'username': '用户名'
# }
def post_new_comment(request):
    if request.method == 'POST':
        food_name = request.POST.get('food_name')
        if request.GET.contains('replied'):
            replied = request.POST.get('replied')
        else:
            replied = None
        comment = request.POST.get('comment')
        username = request.POST.get('username')
        user = User.objects.filter(username=username)
        food = FoodInfo.objects.filter(foodName=food_name)
        FoodComments.objects.create(food=food, replied=replied, user=user, comment=comment)
        return JsonResponse({'code': 200, 'msg': '评论成功'})
    else:
        return JsonResponse({'code': 400, 'msg': '请求方式错误'})
