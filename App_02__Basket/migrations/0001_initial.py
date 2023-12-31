# Generated by Django 4.2.5 on 2023-09-25 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("App_05__Product", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("App_04__Core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="OffCode",
            fields=[
                (
                    "id",
                    models.CharField(max_length=75, primary_key=True, serialize=False),
                ),
                ("code", models.CharField(max_length=6)),
                ("percentage", models.FloatField(default=0.0)),
                ("multiple_used", models.BooleanField(default=True)),
                ("used_status", models.BooleanField(default=False)),
                ("expire_date", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="BasketItem",
            fields=[
                (
                    "id",
                    models.CharField(max_length=75, primary_key=True, serialize=False),
                ),
                ("product_number", models.IntegerField(default=1)),
                ("product", models.ManyToManyField(to="App_05__Product.product")),
            ],
        ),
        migrations.CreateModel(
            name="Basket",
            fields=[
                (
                    "id",
                    models.CharField(max_length=75, primary_key=True, serialize=False),
                ),
                ("total_price", models.FloatField(default=0.0)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Ordering", "Ordering"),
                            ("Finalization", "Finalization"),
                            ("Successful", "Successful"),
                            ("Cancel", "Cancel"),
                        ],
                        max_length=15,
                    ),
                ),
                ("date", models.DateTimeField()),
                (
                    "address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="App_04__Core.address",
                    ),
                ),
                (
                    "off_code",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="App_02__Basket.offcode",
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
    ]
