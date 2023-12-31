# Generated by Django 4.2.5 on 2023-09-25 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("App_05__Product", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProductHistory",
            fields=[
                (
                    "id",
                    models.CharField(max_length=75, primary_key=True, serialize=False),
                ),
                ("date", models.DateTimeField()),
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
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserInf",
            fields=[
                (
                    "id",
                    models.CharField(max_length=75, primary_key=True, serialize=False),
                ),
                (
                    "user_type",
                    models.CharField(
                        choices=[("admin", "admin"), ("customer", "customer")],
                        max_length=10,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ForgotPassword",
            fields=[
                (
                    "id",
                    models.CharField(max_length=75, primary_key=True, serialize=False),
                ),
                ("expire_time", models.DateTimeField()),
                ("code", models.CharField(max_length=6)),
                ("status", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.CharField(max_length=75, primary_key=True, serialize=False),
                ),
                ("address", models.TextField()),
                ("country", models.CharField(max_length=25)),
                ("city", models.CharField(max_length=25)),
                ("phone_number", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254)),
                ("postal_code", models.CharField(max_length=16)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
