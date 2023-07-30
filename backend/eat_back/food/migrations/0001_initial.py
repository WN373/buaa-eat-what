# Generated by Django 4.2.3 on 2023-07-29 06:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("taggit", "0005_auto_20220424_2025"),
    ]

    operations = [
        migrations.CreateModel(
            name="CounterInfo",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("counter_name", models.CharField(max_length=128, verbose_name="柜台名")),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FoodInfo",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "food_name",
                    models.CharField(max_length=128, unique=True, verbose_name="菜品名"),
                ),
                (
                    "price",
                    models.CharField(default="0.0", max_length=64, verbose_name="价格"),
                ),
                ("comments", models.IntegerField(default=0, verbose_name="评论数")),
                ("rating", models.FloatField(default=0.0, verbose_name="评分")),
                ("stars", models.IntegerField(default=0, verbose_name="收藏量")),
                ("purchases", models.IntegerField(default=0, verbose_name="购买量")),
                (
                    "photo_url",
                    models.CharField(
                        blank=True, default="", max_length=256, verbose_name="图片地址"
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "counter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="food.counterinfo",
                        verbose_name="柜台",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RegionInfo",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "region_name",
                    models.CharField(max_length=128, unique=True, verbose_name="地区名"),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RegionFavor",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="收藏时间"),
                ),
                (
                    "region",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="food.regioninfo",
                        verbose_name="地区",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="用户",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FoodPurchase",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("rating", models.IntegerField(default=0, verbose_name="评分")),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="购买时间"),
                ),
                (
                    "food",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="food.foodinfo",
                        verbose_name="菜品",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="用户",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="foodinfo",
            name="region",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="food.regioninfo",
                verbose_name="地区",
            ),
        ),
        migrations.AddField(
            model_name="foodinfo",
            name="tags",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="标签",
            ),
        ),
        migrations.CreateModel(
            name="FoodFavor",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="收藏时间"),
                ),
                (
                    "food",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="food.foodinfo",
                        verbose_name="菜品",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="用户",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FoodComments",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("comment", models.CharField(max_length=256, verbose_name="评论内容")),
                (
                    "is_anonymous",
                    models.BooleanField(blank=True, default=False, verbose_name="是否匿名"),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="评论时间"),
                ),
                (
                    "food",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="food.foodinfo",
                        verbose_name="菜品",
                    ),
                ),
                (
                    "replied",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="food.foodcomments",
                        verbose_name="回复",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="用户",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="counterinfo",
            name="region",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="food.regioninfo",
                verbose_name="地区",
            ),
        ),
        migrations.CreateModel(
            name="CounterFavor",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="收藏时间"),
                ),
                (
                    "counter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="food.counterinfo",
                        verbose_name="柜台",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="用户",
                    ),
                ),
            ],
        ),
    ]