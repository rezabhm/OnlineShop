from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.OffCode)
admin.site.register(models.Basket)
admin.site.register(models.BasketItem)
