# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('add-to-wishlist/', addToWishlist, name='add-to-wishlist'),
    path('delete-from-wishlist/', deleteFromWishlist,
         name='delete-from-wishlist'),
]
