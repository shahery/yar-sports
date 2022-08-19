from django.urls import path
from .views import *

urlpatterns = [
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
]