from App_03__Category import models
from App_05__Product import models as prd_model
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from  . import serializer


def product_image_list(product_id):

    """

        return product list by category

    """

    try:

        product_obj = prd_model.Product.objects.get(id=product_id)
        product_serializer = serializer.ProductSerializer(data=[product_obj], many=True)
        product_serializer.is_valid()

        prod_list = prd_model.ProductImage.objects.filter(product=product_obj)
        prod_list_serializer = serializer.ProductListSerializer(data=prod_list, many=True)
        prod_list_serializer.is_valid()

        return {

            'status': True,
            'result': "product exist , (محصول مورد نظر یافت شد)",
            'main-product-image': product_serializer.data,
            'product-image-list': prod_list_serializer.data

        }

    except:

        return {

            'status': False,
            'result': "product didn't exist , (محصول مورد نظر یافت نشد)",

        }
