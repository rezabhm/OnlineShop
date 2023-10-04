from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from . import serializer


# Home API in views
class SignUpCustomer(generics.CreateAPIView):

    """

        signup new customer user (ثبت نام کاربران مشتری )

    """

    permission_classes = (AllowAny,)
    serializer_class = serializer.SignUpSerializer
