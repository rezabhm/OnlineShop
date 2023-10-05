from App_03__Category import models
from App_05__Product import models as prd_model
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from  . import serializer
from . import serializer as prod_serial


def product_image_list(product_id):

    """

        return product image list

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


def product_inf(product_id):

    """

        return product description

    """

    try:

        product_obj = prd_model.Product.objects.get(id=product_id)
        product_serializer = prod_serial.Product(data=[product_obj], many=True)
        product_serializer.is_valid()

        return {

            'status': True,
            'result': "product exist , (محصول مورد نظر یافت شد)",
            'product-inf': product_serializer.data,

        }

    except:

        return {

            'status': False,
            'result': "product didn't exist , (محصول مورد نظر یافت نشد)",

        }


def product_color_size(product_id):

    """

        return product color and size

    """

    try:

        # get product size list
        product_size_list = prd_model.Size.objects.filter(color__product__id=product_id)

        # create product list data
        product_list = {}
        for sz in product_size_list:

            sz_serial = serializer.ProductSizeSerializer(data=[sz], many=True)
            sz_serial.is_valid()

            try:

                product_list[sz.color.id].append(sz_serial.data[0])

            except:

                product_list[sz.color.id] = [sz_serial.data[0]]

        return {

            'status': True,
            'result': "product exist , (محصول مورد نظر یافت شد)",
            'product-size-color': product_list,

        }

    except:

        return {

            'status': False,
            'result': "product didn't exist , (محصول مورد نظر یافت نشد)",

        }
