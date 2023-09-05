from django.db import models
from django.contrib.auth.models import User

from Product import models as product_model
from Core import models as core_model


# Create your models here.


class OffCode(models.Model):
    """

        off code table

    """

    id = models.CharField(max_length=75, primary_key=True)

    code = models.CharField(max_length=6)
    percentage = models.FloatField(default=0.0)

    multiple_used = models.BooleanField(default=True)
    used_status = models.BooleanField(default=False)

    expire_date = models.DateTimeField()

    def __str__(self):
        return self.code


class Basket(models.Model):

    """

    basket table for store user's buying information

    """

    id = models.CharField(max_length=75, primary_key=True)

    total_price = models.FloatField(default=0.0)

    status_tuple = (

        ('Ordering', 'Ordering'),
        ('Finalization', 'Finalization'),
        ('Successful', 'Successful'),
        ('Cancel', 'Cancel'),

    )
    status = models.CharField(max_length=15, choices=status_tuple)

    date = models.DateTimeField()

    off_code = models.ForeignKey(OffCode, on_delete=models.PROTECT)
    address = models.ForeignKey(core_model.Address, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.id


class BasketItem(models.Model):

    """

        table for store basket item that user selected

    """

    id = models.CharField(max_length=75, primary_key=True)

    product_number = models.IntegerField(default=1)

    product = models.ManyToManyField(product_model.Product)

    def __str__(self):
        return self.id
