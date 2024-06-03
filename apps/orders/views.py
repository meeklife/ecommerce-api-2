from rest_framework.viewsets import ModelViewSet

from .models import Order, OrderItem, Transaction
from .serializers import OrderItemSerializer, OrderSerializer, TransactionSerializer


class Transactions(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    http_method_names = [m for m in ModelViewSet.http_method_names if m not in ["put"]]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class Orders(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    http_method_names = [m for m in ModelViewSet.http_method_names if m not in ["put"]]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderItems(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    http_method_names = [m for m in ModelViewSet.http_method_names if m not in ["put"]]
