from rest_framework import serializers
from apps.cart.models import ShoppingCart, CartItem
from apps.products.models import Product
from apps.products.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    cart = serializers.PrimaryKeyRelatedField(read_only=True)
    # product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    # product_details = serializers.CharField(source="product", read_only=True)
    product = ProductSerializer()

    class Meta:
        model: CartItem
        fields = "_all__"


class ShoppingCartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = ShoppingCart
        fields = ["id", "user", "items"]
