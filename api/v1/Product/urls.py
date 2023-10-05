from django.urls import re_path
from api.v1.Product import views as api


urlpatterns = [

    re_path(r'^product-image-list/product-id=(?P<product_id>[\w]+)/', api.ProductImageList.as_view()),

]
