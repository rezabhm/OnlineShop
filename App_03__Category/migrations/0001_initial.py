# Generated by Django 4.2.5 on 2023-09-25 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CategoryRoot",
            fields=[
                (
                    "id",
                    models.CharField(max_length=75, primary_key=True, serialize=False),
                ),
                ("title", models.CharField(max_length=25)),
                ("visualize_status", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="CategorySubRoot",
            fields=[
                (
                    "id",
                    models.CharField(max_length=75, primary_key=True, serialize=False),
                ),
                ("title", models.CharField(max_length=25)),
                ("visualize_status", models.BooleanField(default=True)),
                (
                    "category_root",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="App_03__Category.categoryroot",
                    ),
                ),
            ],
        ),
    ]
