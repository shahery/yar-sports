# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class WishItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, null=True, blank=True)
    quantity = models.SmallIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product}"
