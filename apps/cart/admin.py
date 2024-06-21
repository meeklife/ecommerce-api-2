from django.contrib import admin

from apps.cart.models import CartItem, ShoppingCart

admin.site.register(CartItem)
admin.site.register(ShoppingCart)
