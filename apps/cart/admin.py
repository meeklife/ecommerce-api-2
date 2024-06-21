from django.contrib import admin
from apps.cart.models import ShoppingCart, CartItem

admin.site.register(CartItem)
admin.site.register(ShoppingCart)
