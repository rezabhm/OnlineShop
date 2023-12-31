from App_03__Category import models
from App_05__Product import models as prd_model
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from  . import serializer


def category_list():

    """

        return category list

    """

    sub_category_list = models.CategorySubRoot.objects.filter(visualize_status=True)

    category_data = {}
    for dt in sub_category_list:

        # get category root name
        category_name = dt.category_root.title

        # append category sub root to category list
        if category_name in category_data.keys():
            category_data[category_name].append(dt.title)
        else:
            category_data[category_name] = [dt.title]

    return {'category_list': category_data}


def account_information(request):

    user_id = Token.objects.get(key=request.auth.key).user_id
    user = User.objects.get(id=user_id)

    user_serializer = serializer.AccountInfoSerializer(data=[user], many=True)

    user_serializer.is_valid()

    return user_serializer.data[0]


def product_list(category):

    """

        return product list by category

    """

    product_obj_list = prd_model.Product.objects.filter(category_root__title=category)[:6]
    product_list_serializer = serializer.ProductList(data=product_obj_list, many=True)
    product_list_serializer.is_valid()

    return {

        'product-list': product_list_serializer.data
    }
