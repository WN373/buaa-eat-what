# Generated by Django 4.2.3 on 2023-07-26 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodName', models.CharField(max_length=128, verbose_name='菜品名')),
                ('parentName', models.CharField(max_length=128, unique=True, verbose_name='餐厅名')),
                ('price', models.FloatField(verbose_name='价格')),
                ('stars', models.IntegerField(verbose_name='收藏量')),
                ('purchases', models.IntegerField(verbose_name='购买量')),
            ],
        ),
        migrations.CreateModel(
            name='UsrInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usrName', models.CharField(max_length=128, verbose_name='用户名')),
                ('usrGender', models.BooleanField(verbose_name='性别')),
            ],
        ),
    ]
