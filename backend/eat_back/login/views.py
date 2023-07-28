from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout, models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# GPT assisted

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return JsonResponse({'code': 200, 'msg': '登录成功'})
        else:
            errors = dict(form.errors.items())
            return JsonResponse({'code': 400, 'msg': '登录失败', 'errors': errors})
    else:
        form = AuthenticationForm()
    return JsonResponse({'code': 400, 'msg': '请求方式错误'})


@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return JsonResponse({'code': 200, 'msg': '注册成功'})
        else:
            errors = dict(form.errors.items())
            return JsonResponse({'code': 400, 'msg': '注册失败', 'errors': errors})
    else:
        form = UserCreationForm()
    return JsonResponse({'code': 400, 'msg': '请求方式错误'})

# modify_password
# /login/modify/
# post:
# {
#    'username': '用户名',
#    'password': '新密码'
# }
@csrf_exempt
def modify_password(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            user = models.User.objects.get(username=username)
            password = request.POST.get('password')
            print('modifying',username, password)
            user.set_password(password)
            user.save()
            return JsonResponse({'code': 200, 'msg': '修改成功'})
        except Exception as e:
            return JsonResponse({'code': 400, 'msg': '修改失败', 'error': str(e)})
    else:
        return JsonResponse({'code': 400, 'msg': '请求方式错误'})

def logout_view(request):
    logout(request)
    return redirect('index')

def index(request):
    return HttpResponse('login index')
