from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import Order, OrderItem
from .serializers import OrderItemSerializer, OrderSerializer


class Orders(
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return self.queryset
        return Order.objects.filter(user=user)


class OrderItems(
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return self.queryset
        return OrderItem.objects.filter(order__user=user)
