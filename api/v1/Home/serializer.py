from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth.models import User
from App_05__Product import models


class AccountInfoSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ['username', 'first_name', 'last_name']


class ProductList(serializers.ModelSerializer):

    category_root = serializers.CharField(required=True, validators=[validate_password])

    class Meta:

        model = models.Product
        fields = ['id', 'title', 'image', 'price', 'description', 'category_root']

    def validate(self, attrs):
        """

            validate password with confirm password

        """

        attrs['category_root'] = models.category_model.objects.get(id=attrs['category_root']).title

        return attrs
