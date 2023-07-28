from django.shortcuts import render

# Create your views here.
from .models import *
from django.http import JsonResponse
from .forms import FoodInfoForm
from django.views.decorators.csrf import csrf_exempt

# create_food_favor
# post:
# {
#     'food_name': '菜品名称',
#     'username': '用户名',
# }
@csrf_exempt
def create_food_favor(request):
    if request.method == 'POST':
        try:
            food_name = request.POST.get('food_name')
            food = FoodInfo.objects.filter(food_name=food_name)
            username = request.POST.get('username')
            user = User.objects.filter(username=username)
            food_favor = FoodFavor(food=food)
            food_favor.save()
            return JsonResponse({'code': 200, 'msg': '创建成功'})
        except Exception as e:
            return JsonResponse({'code': 400, 'msg': '创建失败', 'error': str(e)})
    else:
        return JsonResponse({'code': 400, 'msg': '请求方式错误'})


# create_food
# post:
# {
#     'food_name': '菜品名称',
#     'price': '价格',
#     'tags': '标签',
#     'food_url': '图片地址',
# }
@csrf_exempt
def create_food(request):
    if request.method == 'POST':
        form = FoodInfoForm(request.POST)
        if form.is_valid():
            form.save()
            try:
                print(form.cleaned_data['id'])
            finally:
                return JsonResponse({'code': 200, 'msg': '创建成功'})
        else:
            return JsonResponse({'code': 400, 'msg': '创建失败(您的表单格式可能错误)', 'error': str(form.errors)})
    else:
        return JsonResponse({'code': 400, 'msg': '请求方式错误'})

# get:
# { 'food_name': '菜品名称' }
def get_food_by_name(request):
    if request.method == 'GET':
        food_name = request.GET.get('food_name')
        foods = FoodInfo.objects.filter(food_name=food_name)
        print(len(foods), food_name)
        data = [{
            'id': food.id,
            'food_name': food.food_name,
            'price': food.price,
            'tags': ', '.join(food.tags.values_list('name', flat=True)),
            'rating': food.rating,
            'stars': food.stars,
            'purchases': food.purchases,
            'created': food.created
        } for food in foods]
        print(data)
        return JsonResponse({'code': 200, 'msg': '获取成功', 'data': data}, safe=False)
    else:
        return JsonResponse({'code': 400, 'msg': '请求方式错误'})


@csrf_exempt
def create_purchase(request):
    if request.method == 'POST':
        food_name = request.POST.get('food_name')
        food = FoodInfo.objects.filter(food_name=food_name)
        purchase = FoodPurchase(food=food)
        purchase.save()
        return JsonResponse({'code': 200, 'msg': '创建成功'})


# get_comment_list
# /food/comment/
# get:
# {
#    'food_name': '菜品名称',
# }
def get_comment_list(request):
    if request.method == 'GET':
        food_name = request.GET.get('food_name')
        food = FoodInfo.objects.get(food_name=food_name)
        comments = FoodComments.objects.filter(food=food).order_by('-created')
        comment_list = [{
            'id': comment.id,
            'comment': comment.comment,
            'username': comment.user.username,
            'is_anonymous': comment.is_anonymous,
            'replied': comment.replied.username if comment.replied else None,
            'created': comment.created
        } for comment in comments]
        return JsonResponse({'code': 200, 'msg': '获取评论成功', 'data': comment_list})
    else:
        return JsonResponse({'code': 400, 'msg': '请求方式错误'})


# post_new_comment
# format:
# {
#     'food_name': '事物名称',
#     'replied': '回复对象',
#     'comment': '评论内容',
#     'username': '用户名',
#     'is_anonymous': '是否匿名'
# }
@csrf_exempt
def post_new_comment(request):
    if request.method == 'POST':
        try:
            food_name = request.POST.get('food_name')
            if 'replied' in request.POST.keys():
                replied_name = request.POST.get('replied')
                replied = User.objects.get(username=replied_name).id
            else:
                replied = None
            comment = request.POST.get('comment')
            username = request.POST.get('username')
            user = User.objects.get(username=username)
            food = FoodInfo.objects.get(food_name=food_name)
            FoodComments.objects.create(food_id=food.id, replied_id=replied, user_id=user.id, comment=comment)
            food.comments += 1
            food.save()
            return JsonResponse({'code': 200, 'msg': '评论成功'})
        except Exception as e:
            return JsonResponse({'code': 400, 'msg': '评论失败', 'error': str(e)})
    else:
        return JsonResponse({'code': 400, 'msg': '请求方式错误'})
