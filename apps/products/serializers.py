from rest_framework import serializers

from .models import ProductCategory, Products


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ["id", "name", "description"]


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = [
            "id",
            "name",
            "description",
            "price",
            "specification",
            "brand",
            "category",
        ]

    def get_brand(self, product) -> str:
        return product.brand.name if product.brand else ""

    def get_category(self, product):
        return product.category.name if product.category else ""
