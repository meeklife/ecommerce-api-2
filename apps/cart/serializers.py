from rest_framework import serializers

from apps.cart.models import CartItem, ShoppingCart
from apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']


class CartItemSerializer(serializers.ModelSerializer):
    # cart = serializers.PrimaryKeyRelatedField(read_only=True)
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ["id", "product", "price", "quantity"]


class ShoppingCartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = ShoppingCart
        fields = ["id", "user", "items"]
