from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.CategoryRoot)
admin.site.register(models.CategorySubRoot)
