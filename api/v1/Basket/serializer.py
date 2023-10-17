from rest_framework import serializers
from django.contrib.auth.models import User
from App_05__Product import models
from App_03__Category import models as category_model
from django.contrib.auth.password_validation import validate_password
#
#
# class Product(serializers.ModelSerializer):
#
#     category_root = serializers.CharField(required=True, validators=[validate_password])
#
#     class Meta:
#
#         model = models.Product
#         fields = ['id', 'title', 'price', 'description', 'category_root']
#
#     def validate(self, attrs):
#         """
#
#             validate password with confirm password
#
#         """
#
#         attrs['category_root'] = models.category_model.objects.get(id=attrs['category_root']).title
#
#         return attrs


