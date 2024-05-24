from rest_framework import serializers

from ..brands.models import Brand
from .models import ProductCategory, ProductImage, Products


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ["id", "name", "description"]


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all())
    category = serializers.PrimaryKeyRelatedField(
        queryset=ProductCategory.objects.all()
    )
    brand_name = serializers.CharField(source="brand.name", read_only=True)
    category_name = serializers.CharField(source="category.name", read_only=True)

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


class ProductImageSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Products.objects.all())
    product_name = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = ProductImage
        fields = ["id", "product", "product_name", "product_image"]
