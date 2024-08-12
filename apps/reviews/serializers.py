from rest_framework import serializers

from apps.products.models import Product
from apps.reviews.models import AppReview, ProductReview
from apps.users.serializers import UserSerializer


class ProductReviewSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    user_details = serializers.CharField(source="user.username", read_only=True)
    product_details = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = ProductReview
        fields = [
            "id",
            "user",
            "user_details",
            "product",
            "product_details",
            "rating",
            "description",
        ]


class AppReviewSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    user_details = UserSerializer(source="user", read_only=True)

    class Meta:
        model = AppReview
        fields = ["id", "user", "user_details", "rating", "description"]
