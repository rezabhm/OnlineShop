from django.urls import re_path
from api.v1.Authentication import views as api
from rest_framework.authtoken import views


urlpatterns = [

    re_path('^sign-up/', api.SignUpCustomer.as_view()),
    re_path('^login/', views.obtain_auth_token),

]
