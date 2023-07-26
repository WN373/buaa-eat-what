from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class ViewsTest(TestCase):

    def setUp(self):
        self.client = Client()

        # 创建测试用户
        self.username = 'testuser'
        self.password = 'testpass'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )

    def test_login_view(self):
        # 测试登录页面的 GET 请求
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, 'login.html')

        # 测试登录页面的 POST 请求（正确的登录信息）
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': self.password
        })
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'code': 200, 'msg': '登录成功'})

        # 测试登录页面的 POST 请求（错误的登录信息）
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': 'wrongpass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'code': 400, 'msg': '登录失败', 'errors': {'__all__': ['Please enter a correct username and password. Note that both fields may be case-sensitive.']}})

    def test_register_view(self):
        # 测试注册页面的 GET 请求
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, 'register.html')

        # 测试注册页面的 POST 请求（正确的注册信息）
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'newpass123',
            'password2': 'newpass123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'code': 200, 'msg': '注册成功'})

        # 测试注册页面的 POST 请求（错误的注册信息）
        response = self.client.post(reverse('register'), {
            'username': '',
            'password1': 'newpass123',
            'password2': 'wrongpass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'code': 400, 'msg': '注册失败', 'errors': {'username': ['This field is required.'], 'password2': ['The two password fields didn’t match.']}})

    def test_logout_view(self):
        # 测试退出登录
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('index'))

    def test_index(self):
        # 测试主页面
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '主页面')