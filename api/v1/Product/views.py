from django.http import JsonResponse
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

from . import utils
from  . import serializer


# Home API in views
class ProductImageList(APIView):

    """

        return Product Image List ( تصاویر محصول را میدهد )

    """
    permission_classes = (AllowAny,)

    def get(self, request, product_id):

        data = utils.product_image_list(product_id)

        return JsonResponse(data, status=200)


class ProductInformation(APIView):

    """

        return Product Description ( اطلاعات محصول را میدهد )

    """

    permission_classes = (AllowAny,)

    def get(self, request, product_id):

        data = utils.product_inf(product_id)

        return JsonResponse(data, status=200)


class ProductColorSize(APIView):

    """

        return Product Color and Size ( اطلاعات رنگ و سایز محصول را میدهد  )

    """

    permission_classes = (AllowAny,)

    def get(self, request, product_id):

        data = utils.product_color_size(product_id)

        return JsonResponse(data, status=200)


class SuggestionProductList(APIView):

    """

        return Product suggestion list ( لیست محصولات مشابه را میدهد )

    """

    def get(self, request, product_id):

        data = utils.suggestion_product_list(product_id)

        return JsonResponse(data, status=200)
