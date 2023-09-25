from django.contrib import admin
from . import models

# Register your models here.
admin.register(models.Size)
admin.register(models.Color)
admin.register(models.Product)
admin.register(models.ProductImage)
admin.register(models.ProductVote)
