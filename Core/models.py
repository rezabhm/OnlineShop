from django.db import models
from django.contrib.auth.models import User

from Product import models as product_model

# Create your models here.


class UserInf(models.Model):

    """

        additional information for user

    """

    id = models.CharField(max_length=75, primary_key=True)

    user_type_tuple = (

        ('admin', 'admin'),
        ('customer', 'customer')

    )
    user_type = models.CharField(max_length=10, choices=user_type_tuple)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class UserProductHistory(models.Model):

    """

        user product history for store every product visit of user

    """

    id = models.CharField(max_length=75, primary_key=True)

    date = models.DateTimeField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product_model.Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class ForgotPassword(models.Model):

    """

        this table will help to handle forgot password process

    """

    id = models.CharField(max_length=75, primary_key=True)

    expire_time = models.DateTimeField()

    code = models.CharField(max_length=6)
    status = models.BooleanField(default=False)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.code


class Address(models.Model):

    """

        save user address for basket

    """

    id = models.CharField(max_length=75, primary_key=True)

    address = models.TextField()
    country = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    postal_code = models.CharField(max_length=16)

    user = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return self.address
