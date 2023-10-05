from rest_framework import serializers
from django.contrib.auth.models import User
from App_05__Product import models


class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.Product
        fields = ['id', 'image']


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.Product
        fields = ['id', 'image']

