from rest_framework import serializers

from apps.inventory.models import Inventory
from apps.users.models import Address

from .models import Order, OrderItem, Transaction


class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Transaction
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    delivery_address = serializers.PrimaryKeyRelatedField(
        queryset=Address.objects.all()
    )

    class Meta:
        model = Order
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    inventory = serializers.PrimaryKeyRelatedField(queryset=Inventory.objects.all())

    class Meta:
        model = OrderItem
        fields = "__all__"
