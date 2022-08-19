from django.shortcuts import render
from django.views import generic
from .models import *


class WishlistView(generic.View):
    def get(self, *arg, **kwargs):
        wish_items = WishItem.objects.filter(user=self.request.user)
        context = {
            'wish_items': wish_items
        }
        return render(self.request, 'wishlist/wishlist.html', context)
