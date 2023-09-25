from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Address)
admin.site.register(models.UserInf)
admin.site.register(models.ForgotPassword)
admin.site.register(models.UserProductHistory)
