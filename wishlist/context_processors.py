# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from wishlist.models import *


def add_variable_to_context(request):
    if request.user.is_authenticated:
        return {
            'wish_count': WishItem.objects.filter(user=request.user).count()
        }
    else:
        return {
            'wish_count': 0
        }
