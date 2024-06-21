from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from apps.cart.models import CartItem, ShoppingCart
from apps.cart.serializers import CartItemSerializer, ShoppingCartSerializer


class ShoppingCartViewSet(ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer

    http_method_names = [m for m in ModelViewSet.http_method_names if m not in ["put"]]


class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    http_method_names = [m for m in ModelViewSet.http_method_names if m not in ["put"]]
