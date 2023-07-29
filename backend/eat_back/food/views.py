from django.shortcuts import render

# Create your views here.
from .models import *
from django.http import JsonResponse
from .forms import FoodInfoForm
from django.views.decorators.csrf import csrf_exempt


# create_region
# post:
# {
#     'region_name': '地区名称',
# }
@csrf_exempt
def create_region(request):
    if request.method == 'POST':
        try:
            region_name = request.POST.get('region_name')
            region = RegionInfo(region_name=region_name)
            region.save()
            return JsonResponse({'code': 200, 'msg': '创建成功'})
        except Exception as e:
            return JsonResponse({'code': 400, 'msg': '创建失败', 'error': str(e)})
    else:
        return JsonResponse({'code': 400, 'msg': '请求方式错误'})

# delete_region
# post:
# {
#     'region_name': '地区名称',
# }
@csrf_exempt
def delete_region(request):
    if request.method == 'POST':
        try:
            region_name = request.POST.get('region_name')
            region = RegionInfo.objects.get(region_name=region_name)
            # counters = CounterInfo.objects.filter(region=region)
            # for counter in counters:
            #     counter.delete()
            region.delete()
            return JsonResponse({'code': 200, 'msg': '删除成功'})
        except Exception as e:
            return JsonResponse({'code': 400, 'msg': '删除失败(可能出现未完全的删除，请咨询管理员)', 'error': str(e)})
    else:
        return JsonResponse({'code': 400, 'msg': '请求方式错误'})

# get_regions
# get:
def get_regions(request):
    if request.method == 'GET':
        try:
            regions = RegionInfo.objects.all()
            data = [{
                'id': region.id,
                'region_name': region.region_name,
                'created': region.created,
            } for region in regions]
            return JsonResponse({'code': 200, 'msg': '获取成功', 'data': data})
        except Exception as e:
            return JsonResponse({'code': 400, 'msg': '获取失败', 'error': str(e)})
    else:
        return JsonResponse({'code': 400, 'msg': '请求方式错误'})


# create_counter:
# post:
# {
#     'counter_name': '柜台名称',
#     'region_name': '地区名称',
# }
@csrf_exempt
def create_counter(request):
    if request.method == 'POST':
        try:
            counter_name = request.POST.get('counter_name')
            region_name = request.POST.get('region_name')
            region = RegionInfo.objects.get(region_name=region_name)
            assert CounterInfo.objects.filter(counter_name=counter_name, region=region).exists() is False
            counter = CounterInfo(counter_name=counter_name, region=region)
            counter.save()
            return JsonResponse({'code': 200, 'msg': '创建成功'})
        except Exception as e:
            return JsonResponse({'code': 400, 'msg': '创建失败', 'error': str(e)})
    else:
        return JsonResponse({'code': 400, 'msg': '请求方式错误'})

# delete_counter
# post:
# {
#     'counter_name': '柜台名称',
#     'region_name': '地区名称',
# }
@csrf_exempt
def delete_counter(request):
    if request.method == 'POST':
        try:
            counter_name = request.POST.get('counter_name')
            region_name = request.POST.get('region_name')
            region = RegionInfo.objects.get(region_name=region_name)
            counter = CounterInfo.objects.get(counter_name=counter_name, region=region)
            counter.delete()
            return JsonResponse({'code': 200, 'msg': '删除成功'})
        except Exception as e:
            return JsonResponse({'code': 400, 'msg': '删除失败(可能出现未完全的删除，请咨询管理员)', 'error': str(e)})
    else:
        return JsonResponse({'code': 400, 'msg': '请求方式错误'})

# get_counters_by_region
# get:
# {
#     'region_name': '地区名称',
# }
def get_counters_by_region(request):
    if request.method == 'GET':
        try:
            region_name = request.GET.get('region_name')
            region = RegionInfo.objects.get(region_name=region_name)
            counters = CounterInfo.objects.filter(region=region)
            data = [{
                'id': counter.id,
                'counter_name': counter.counter_name,
                'created': counter.created
            } for counter in counters]
            return JsonResponse({'code': 200, 'msg': '获取成功', 'data': data})
        except Exception as e:
            return JsonResponse({'code': 400, 'msg': '获取失败', 'error': str(e)})
    else:
        return JsonResponse({'code': 400, 'msg': '请求方式错误'})


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
            food = FoodInfo.objects.get(food_name=food_name)
            username = request.POST.get('username')
            user = User.objects.get(username=username)
            food_favor = FoodFavor(food=food, user=user)
            food_favor.save()
            food.stars += 1
            food.save()
            return JsonResponse({'code': 200, 'msg': '创建成功'})
        except Exception as e:
            return JsonResponse({'code': 400, 'msg': '创建失败', 'error': str(e)})
    else:
        return JsonResponse({'code': 400, 'msg': '请求方式错误'})


# delete_food_favor
# post:
# {
#     'food_name': '菜品名称',
#     'username': '用户名',
# }
@csrf_exempt
def delete_food_favor(request):
    if request.method == 'POST':
        try:
            food_name = request.POST.get('food_name')
            food = FoodInfo.objects.get(food_name=food_name)
            username = request.POST.get('username')
            user = User.objects.get(username=username)
            food_favor = FoodFavor.objects.get(food=food, user=user)
            food_favor.delete()
            food.stars -= 1
            food.save()
            return JsonResponse({'code': 200, 'msg': '删除成功'})
        except Exception as e:
            return JsonResponse({'code': 400, 'msg': '删除失败', 'error': str(e)})
    else:
        return JsonResponse({'code': 400, 'msg': '请求方式错误'})


# create_region_favor
# post:
# {
#     'region_name': '地区名称',
#     'username': '用户名',
#     'manipulate': '操作类型', # add | delete
# }
# attention:
#       删除成功时状态码为 201
@csrf_exempt
def modify_region_favor(request):
    if request.method == 'POST':
        try:
            region_name = request.POST.get('region_name')
            region = RegionInfo.objects.get(region_name=region_name)
            username = request.POST.get('username')
            user = User.objects.get(username=username)
            if request.POST.get('manipulate') == 'add':
                region_favor = RegionFavor(region=region, user=user)
                region_favor.save()
                return JsonResponse({'code': 200, 'msg': '创建成功'})
            elif request.POST.get('manipulate') == 'delete':
                region_favor = RegionFavor.objects.get(region=region, user=user)
                region_favor.delete()
                return JsonResponse({'code': 201, 'msg': '删除成功'})
            else:
                raise AttributeError('manipulate参数错误')
        except Exception as e:
            return JsonResponse({'code': 400, 'msg': '操作失败', 'error': str(e)})
    else:
        return JsonResponse({'code': 400, 'msg': '请求方式错误'})


# modify_counter_favor
# post:
# {
#     'counter_name': '柜台名称',
#     'region_name': '地区名称',
#     'username': '用户名',
#     'manipulate': '操作类型', # add | delete
# }
@csrf_exempt
def modify_counter_favor(request):
    if request.method == 'POST':
        try:
            region_name = request.POST.get('region_name')
            region = RegionInfo.objects.get(region_name=region_name)
            username = request.POST.get('username')
            user = User.objects.get(username=username)
            counter_name = request.POST.get('counter_name')
            counter = CounterInfo.objects.get(counter_name=counter_name, region=region)
            if request.POST.get('manipulate') == 'add':
                counter_favor = CounterFavor(counter=counter, user=user)
                counter_favor.save()
                return JsonResponse({'code': 200, 'msg': '创建成功'})
            elif request.POST.get('manipulate') == 'delete':
                counter_favor = CounterFavor.objects.get(counter=counter, user=user)
                counter_favor.delete()
                return JsonResponse({'code': 201, 'msg': '删除成功'})
            else:
                raise AttributeError('manipulate参数错误')
        except Exception as e:
            return JsonResponse({'code': 400, 'msg': '操作失败', 'error': str(e)})
    else:
        return JsonResponse({'code': 400, 'msg': '请求方式错误'})


# get_region_favors
# get:
# {
#    'username': '用户名',
# }
def get_region_favor(request):
    if request.method == 'GET' :
        try:
            username = request.GET.get('username')
            user = User.objects.get(username=username)
            region_favors = RegionFavor.objects.filter(user=user).order_by('-created')
            data = [{
                'id': region_favor.id,
                'region_name': region_favor.region.region_name,
                'username': region_favor.user.username,
                'created': region_favor.created
            } for region_favor in region_favors]
            return JsonResponse({'code': 200, 'msg': '获取成功', 'data': data})
        except Exception as e:
            return JsonResponse({'code': 400, 'msg': '获取失败', 'error': str(e)})
    else:
        return JsonResponse({'code': 400, 'msg': '请求方式错误'})


# get_counter_favors
# get:
# {
#     'region_name': '地区名称',
#     'username': '用户名',
# }
def get_counter_favor(request):
    if request.method == 'GET':
        try:
            username = request.GET.get('username')
            user = User.objects.get(username=username)
            region_name = request.GET.get('region_name')
            region = RegionInfo.objects.get(region_name=region_name)
            counter_favors = CounterFavor.objects.filter(user=user, counter__region=region).order_by('-created')
            data = [{
                'id': counter_favor.id,
                'counter_name': counter_favor.counter.counter_name,
                'username': counter_favor.user.username,
                'created': counter_favor.created
            } for counter_favor in counter_favors]
            return JsonResponse({'code': 200, 'msg': '获取成功', 'data': data})
        except Exception as e:
            return JsonResponse({'code': 400, 'msg': '获取失败', 'error': str(e)})
    else:
        return JsonResponse({'code': 400, 'msg': '请求方式错误'})


# get_food_favor
# get:
# {
#     'username': '用户名',
# }
def get_food_favor(request):
    if request.method == 'GET':
        try:
            username = request.GET.get('username')
            user = User.objects.get(username=username)
            food_favors = FoodFavor.objects.filter(user=user).order_by('-created')
            data = [{
                'id': food_favor.id,
                'food_name': food_favor.food.food_name,
                'username': food_favor.user.username,
                'created': food_favor.created
            } for food_favor in food_favors]
            return JsonResponse({'code': 200, 'msg': '获取成功', 'data': data})
        except Exception as e:
            return JsonResponse({'code': 400, 'msg': '获取失败', 'error': str(e)})
    else:
        return JsonResponse({'code': 400, 'msg': '请求方式错误'})

# create_food
# post:
# {
#     'food_name': '菜品名称',
#     'region_name': '地区名称',
#     'counter_name': '柜台名称',
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
            'region_name': food.region.region_name,
            'counter_name': food.counter.counter_name,
            'tags': ', '.join(food.tags.values_list('name', flat=True)),
            'rating': food.rating,
            'stars': food.stars,
            'purchases': food.purchases,
            'photo_url': food.photo_url,
            'created': food.created
        } for food in foods]
        print(data)
        return JsonResponse({'code': 200, 'msg': '获取成功', 'data': data}, safe=False)
    else:
        return JsonResponse({'code': 400, 'msg': '请求方式错误'})


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



    
# buy_food
# post:
# {
#     'food_name': '菜品名称',
#     'username': '用户名',
# }
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
