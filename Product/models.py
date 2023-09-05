from django.db import models
from django.contrib.auth.models import User

from Category import models as category_model

# Create your models here.


class Product(models.Model):

    """

        product detail

    """

    id = models.CharField(max_length=75, primary_key=True)

    title = models.CharField(max_length=25)
    description = models.TextField()

    price = models.FloatField()

    image = models.ImageField()

    visualize_status = models.BooleanField(default=False)

    category_root = models.ForeignKey(category_model.CategoryRoot, on_delete=models.PROTECT)
    category_sub_root = models.ForeignKey(category_model.CategorySubRoot, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Color(models.Model):

    """

        product color

    """

    id = models.CharField(max_length=75, primary_key=True)

    color = models.CharField(max_length=16)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.color


class Size(models.Model):

    """

        define size for product

    """

    id = models.CharField(max_length=75, primary_key=True)

    size = models.CharField(max_length=25)
    stock_number = models.IntegerField(default=1)

    visualize_status = models.BooleanField(default=True)

    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    def __str__(self):

        return self.size


class ProductImage(models.Model):

    """

        image for product

    """

    id = models.CharField(max_length=75, primary_key=True)

    image = models.ImageField()
    visualize_status = models.BooleanField(default=True)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.image


class ProductVote(models.Model):

    """

        store user's vote for product

    """

    id = models.CharField(max_length=75, primary_key=True)

    vote = models.IntegerField()

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
