from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from . import utils


# Home API in views

class CategoryList(APIView):

    permission_classes = (AllowAny,)

    def get(self, request):

        data = utils.category_list()

        return JsonResponse(data, status=200)
