from django.urls import re_path
from api.v1.Home import views as api


urlpatterns = [

    re_path('^account-info/', api.AccountInfo.as_view()),
    re_path('^category-list/', api.CategoryList.as_view()),

]
