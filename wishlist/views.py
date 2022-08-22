from django.shortcuts import render, reverse
from django.views import generic
from .models import Product, WishItem
from django.http import HttpResponseRedirect


class WishlistView(generic.View):

    def get(self, *arg, **kwargs):
        wish_items = WishItem.objects.filter(user=self.request.user)
        context = {
            'wish_items': wish_items
        }
        return render(self.request, 'wishlist/wishlist.html', context)


def addToWishlist(request):
    if request.method=="POST":
        product_var_id = request.POST.get('product-id')
        product_var = Product.objects.get(id=product_var_id)

        try:
            wish_item = WishItem.objects.get(user=request.user, product=product_var)
            if wish_item:
                wish_item.quantity += 1
                wish_item.save()
        except:
            WishItem.objects.create(user=request.user, product=product_var)
        finally:
            return HttpResponseRedirect(reverse('wishlist'))


def deleteFromWishlist(request):
    if request.method=="POST":
        item_id = request.POST.get('item-id')
        WishItem.objects.filter(id=item_id).delete()
        return HttpResponseRedirect(reverse('wishlist'))