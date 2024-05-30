from rest_framework import serializers

from ..products.models import Products
from .models import Inventory


class InventorySerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Products.objects.all())
    product_name = serializers.CharField(source="product", read_only=True)

    class Meta:
        model = Inventory
        fields = [
            "id",
            "product",
            "product_name",
            "price",
            "quantity",
            "original_price",
        ]
