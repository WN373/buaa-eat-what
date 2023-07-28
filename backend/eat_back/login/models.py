from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.
from django.db import models


# class Account(models.Model):
#     password = models.CharField(max_length=200)
#     username = models.CharField(max_length=200)
#     userid = models.CharField(max_length=20)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email) # 将用户输入的邮箱转换为小写

# class Account(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length=255, unique=True)
#     username = models.CharField(max_length=20, unique=True)
#     userid = models.CharField(max_length=20, unique=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(auto_now_add=True)

