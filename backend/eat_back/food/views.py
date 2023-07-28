from django.shortcuts import render

# Create your views here.
from .models import *
from django.http import JsonResponse
from .forms import FoodInfoForm
from django.views.decorators.csrf import csrf_exempt

# create_food
# post:
# {
#     'food_name': '菜品名称',
#     'price': '价格',
#     'tags': '标签'
# }
@csrf_exempt
def create_food(request):
    if request.method == 'POST':
        form = FoodInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'code': 200, 'msg': '创建成功'})
        else:
            return JsonResponse({'code': 400, 'msg': '创建失败(您的表单格式可能错误)', 'error': '???'})
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




# get_food_list
# format:
# {
#    'food_name': '菜品名称',
# }
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
    
    

def buy_food(request):
    if request.method == 'POST':
        food_name = request.POST.get('food_name')
        username = request.POST.get('username')
        user = User.objects.filter(username=username)
        food = FoodInfo.objects.filter(food_name=food_name)
        if len(user) == 0:
            return JsonResponse({'code': 400, 'msg': '未找到用户'})
        if len(food) == 0:
            return JsonResponse({'code': 400, 'msg': '未找到食物'})
        else:
            FoodPurchase.objects.create(food=food[0], user=user[0])
            return JsonResponse({'code': 200, 'msg': food_name})
    else:
        return JsonResponse({'code': 400, 'msg': request.method})
        
        
