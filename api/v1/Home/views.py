from django.http import JsonResponse
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

from . import utils
from  . import serializer


# Home API in views
class CategoryList(APIView):

    """

        return product category list ( لیست دسته بندی محصولات را بر میگرداند )

    """
    permission_classes = (AllowAny,)

    def get(self, request):

        data = utils.category_list()

        return JsonResponse(data, status=200)


class AccountInfo(APIView):

    """

        return summerier account's information ( مختصری از اطلاعات کاربران را میدهد )

    """

    permission_classes = (IsAuthenticated,)
    authentication_classes = [TokenAuthentication]

    def get(self, request):

        data = utils.account_information(request)

        return JsonResponse(data, status=200, safe=False)


class ProductList(APIView):

    """

        return list of product for home page ( لیست محصولات برای صفحه home را میدهد )

    """

    permission_classes = (AllowAny,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request, category):

        data = utils.product_list(category)

        return JsonResponse(data, status=200, safe=False)
