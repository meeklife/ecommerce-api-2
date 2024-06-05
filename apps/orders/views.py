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


class OrderItems(
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
