from rest_framework import serializers
from django.contrib.auth.models import User
from App_05__Product import models


class AccountInfoSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ['username', 'first_name', 'last_name']


class ProductList(serializers.ModelSerializer):

    class Meta:

        model = models.Product
        fields = ['id', 'title', 'image', 'price', 'description', 'category_root']
