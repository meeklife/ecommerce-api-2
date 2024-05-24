from rest_framework import serializers

from ..products.models import Products
from ..products.serializers import ProductSerializer
from ..users.models import User
from ..users.serializers import UserSerializer
from .models import ProductReview


class ProductReviewSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Products.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    user_details = UserSerializer(source="user", read_only=True)
    product_details = ProductSerializer(source="product", read_only=True)

    class Meta:
        model = ProductReview
        fields = ["id", "user", "user_name", "product_name", "product"]
