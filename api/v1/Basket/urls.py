from django.urls import re_path
from api.v1.Basket import views as api


urlpatterns = [

    re_path(r'^add-to-basket/', api.AddToBasket.as_view()),

]
