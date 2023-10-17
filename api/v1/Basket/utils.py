import datetime
import uuid

from App_02__Basket import models
from App_05__Product import models as prd_model
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from  . import serializer
from . import serializer as prod_serial


def add_to_basket(product_size_id, product_number, user):

    """

        add product to user's basket

    """

    # check basket exist or not

    try:

        # get basket with ordering status to add product to this basket
        basket_obj = models.Basket.objects.filter(status='Ordering')[0]

    except:

        # create new basket
        basket_obj = models.Basket()

        basket_obj.id = str(uuid.uuid4().int)
        basket_obj.total_price = 0.0
        basket_obj.date = datetime.datetime.now()
        basket_obj.user = user

        basket_obj.save()

    # get product object
    try:

        size_obj = prd_model.Size.objects.get(id=product_size_id)
        color_obj = size_obj.color
        product_obj = color_obj.product

    except:

        return {

            'status': 400,
            'status_text': ' wrong product-size-id'

        }

    # check product number limitation in warehouse
    if product_number > size_obj.stock_number:

        return {

            'status': 400,
            'status_text': 'product number is out of range'

        }

    # update product number
    size_obj.stock_number -= product_number
    if size_obj.stock_number == 0:

        size_obj.visualize_status = False

    size_obj.save()

    # create basket item obj
    basket_item_obj = models.BasketItem()

    basket_item_obj.id = str(uuid.uuid4().int)
    basket_item_obj.product_number = product_number
    basket_item_obj.product_size = size_obj
    basket_item_obj.basket = basket_obj

    basket_item_obj.save()

    # update basket total price
    basket_obj.total_price += product_obj.price
    basket_obj.save()

    return {

        'status': 200,
        'status_text': 'successfully add to basket'

    }
