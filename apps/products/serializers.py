from rest_framework import serializers

from ..brands.models import Brand
from .models import ProductCategory, Products


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ["id", "name", "description"]


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(
        queryset=Brand.objects.all(), write_only=True
    )
    category = serializers.PrimaryKeyRelatedField(
        queryset=ProductCategory.objects.all(), write_only=True
    )
    brand_name = serializers.SerializerMethodField(read_only=True)
    category_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Products
        fields = [
            "id",
            "name",
            "description",
            "price",
            "specification",
            "brand",
            "brand_name",
            "category",
            "category_name",
        ]

    def get_brand_name(self, product) -> str:
        return product.brand.name if product.brand else ""

    def get_category_name(self, product) -> str:
        return product.category.name if product.category else ""
