from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token

from . import utils
from  . import serializer


# Home API in views
class AddToBasket(APIView):

    """

       this api will get product-size id and add it to basket for user ( محصول را به سبد خرید اضافه میکند )

    """
    permission_classes = (IsAuthenticated,)
    parser_classes = [TokenAuthentication]

    def post(self, request):

        user_id = Token.objects.get(key=request.auth.key).user_id
        user = User.objects.get(id=user_id)

        data = utils.add_to_basket(

            product_size_id=request.post['product_size_id'],
            product_number=request.post['product_number'],
            user=user

        )

        return JsonResponse(data, status=200)
