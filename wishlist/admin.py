# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.contrib import admin
from .models import WishItem

# Register your models here.
admin.site.register(WishItem)
