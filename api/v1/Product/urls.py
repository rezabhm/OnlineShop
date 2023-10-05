from django.urls import re_path
from api.v1.Product import views as api


urlpatterns = [

    re_path(r'^product-image-list/product-id=(?P<product_id>[\w]+)/', api.ProductImageList.as_view()),
    re_path(r'^product-inf/product-id=(?P<product_id>[\w]+)/', api.ProductInformation.as_view()),
    re_path(r'^product-color-size/product-id=(?P<product_id>[\w]+)/', api.ProductColorSize.as_view()),

]
