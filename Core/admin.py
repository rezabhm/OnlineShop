from django.contrib import admin
from . import models

# Register your models here.
admin.register(models.Address)
admin.register(models.UserInf)
admin.register(models.ForgotPassword)
admin.register(models.UserProductHistory)
