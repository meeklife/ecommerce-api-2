from rest_framework import serializers

from ..brands.models import Brand
from ..users.models import User
from .models import Favorite, Product, ProductCategory, ProductImage


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
        model = Product
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
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    product_name = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = ProductImage
        fields = ["id", "product", "product_name", "product_image"]


class FavoriteSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    product_name = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = Favorite
        fields = ["id", "product", "product_name", "user"]
