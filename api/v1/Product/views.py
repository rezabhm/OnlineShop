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
