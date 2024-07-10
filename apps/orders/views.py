from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.db import transaction

from apps.cart.models import CartItem, ShoppingCart
from apps.finance.models import Transaction
from apps.orders.models import Order, OrderItem
from apps.orders.serializers import OrderItemSerializer, OrderSerializer
from apps.users.models import Address
from apps.inventory.models import Inventory


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer

    http_method_names = [
        m for m in ModelViewSet.http_method_names if m not in ["put", "patch"]
    ]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Order.objects.filter(user=user)
        return Order.objects.none()

    @action(detail=False, methods=["post"], url_path="checkout")
    @transaction.atomic
    def checkout(self, request):
        cart = ShoppingCart.objects.filter(user=request.user).first()
        cart_items = CartItem.objects.filter(cart=cart.id)
        if not cart_items:
            return Response({"detail": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST)

        total_amount = sum(item.product.price * item.quantity for item in cart_items)
        delivery_cost = 10

        user_address = Address.objects.filter(user=request.user).first()

        order = Order.objects.create(
            user=request.user,
            delivery_cost=delivery_cost,
            total_cost=total_amount + delivery_cost,
            delivery_address=user_address,
            status='PE'
        )

        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                price=cart_item.price,
            )

        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    @transaction.atomic
    def process_payment(self, request, pk=None):
        order = self.get_object()

        success = True  # I simulated the payment gateway integration

        if success:
            Transaction.objects.create(
                user=request.user,
                order=order,
                amount=order.total_cost,
                status='PA',
                payment_method="CD"
            )

            order.status = 'PC'
            order.save()

            ShoppingCart.objects.filter(user=request.user).delete()

            return Response({"detail": "Payment successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Payment failed"}, status=status.HTTP_400_BAD_REQUEST)
