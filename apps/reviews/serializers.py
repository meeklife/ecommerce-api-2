from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.products.models import Product
from apps.reviews.models import AppReview, ProductReview


class ProductReviewSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    username = serializers.CharField(source="user.username", read_only=True)
    product_name = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = ProductReview
        fields = [
            "id",
            "user",
            "username",
            "product",
            "product_name",
            "rating",
            "description",
        ]


class AppReviewSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = AppReview
        fields = ["id", "user", "username", "rating", "description"]

    def validate(self, data):
        user = self.context["request"].user
        if AppReview.objects.filter(user=user).exists():
            raise ValidationError("You have already reviewed this app.")
        return data
