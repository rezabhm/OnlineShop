# Generated by Django 4.2.5 on 2023-09-25 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("App_03__Category", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Color",
            fields=[
                (
                    "id",
                    models.CharField(max_length=75, primary_key=True, serialize=False),
                ),
                ("color", models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.CharField(max_length=75, primary_key=True, serialize=False),
                ),
                ("title", models.CharField(max_length=25)),
                ("description", models.TextField()),
                ("price", models.FloatField()),
                ("image", models.ImageField(upload_to="")),
                ("visualize_status", models.BooleanField(default=False)),
                (
                    "category_root",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="App_03__Category.categoryroot",
                    ),
                ),
                (
                    "category_sub_root",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="App_03__Category.categorysubroot",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Size",
            fields=[
                (
                    "id",
                    models.CharField(max_length=75, primary_key=True, serialize=False),
                ),
                ("size", models.CharField(max_length=25)),
                ("stock_number", models.IntegerField(default=1)),
                ("visualize_status", models.BooleanField(default=True)),
                (
                    "color",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="App_05__Product.color",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductVote",
            fields=[
                (
                    "id",
                    models.CharField(max_length=75, primary_key=True, serialize=False),
                ),
                ("vote", models.IntegerField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="App_05__Product.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductImage",
            fields=[
                (
                    "id",
                    models.CharField(max_length=75, primary_key=True, serialize=False),
                ),
                ("image", models.ImageField(upload_to="")),
                ("visualize_status", models.BooleanField(default=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="App_05__Product.product",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="color",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="App_05__Product.product",
            ),
        ),
    ]
