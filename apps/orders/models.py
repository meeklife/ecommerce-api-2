from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common import models as base_models
from apps.inventory.models import Inventory
from apps.users import models as usermodels


class Transaction(base_models.BaseModel):
    class Transaction_Status(models.TextChoices):
        PENDING = (
            "PE",
            _("Pending"),
        )
        PAID = (
            "PA",
            _("Paid"),
        )
        REFUNDED = (
            "RE",
            _("Refunded"),
        )
        FAILED = (
            "FA",
            _("Failed"),
        )
        CANCELLED = "CA", _("Cancelled")

    class Payment_Method(models.TextChoices):
        CASH = (
            "CA",
            _("Cash"),
        )
        MOMO = (
            "MO",
            _("Momo"),
        )
        CARD = (
            "CD",
            _("Card"),
        )
        ST_POINTS = "SP", _("St_points")
        REFERRAL_POINTS = "RP", _("Referral_points")

    user = models.ForeignKey(
        usermodels.User, on_delete=models.CASCADE, related_name="transactions"
    )
    status = models.CharField(
        max_length=2,
        choices=Transaction_Status.choices,
        default=Transaction_Status.PENDING,
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(default=datetime.now)
    payment_method = models.CharField(
        max_length=2, choices=Payment_Method.choices, default=Payment_Method.CARD
    )


class Order(base_models.BaseModel):
    class Order_Status(models.TextChoices):
        DRAFT = (
            "D",
            _("Draft"),
        )
        PENDING = (
            "PE",
            _("Pending"),
        )
        PAYMENT_COMPLETE = (
            "PC",
            _("Payment Complete"),
        )
        IN_DELIVERY = (
            "IND",
            _("in-delivery"),
        )
        COMPLETE = (
            "CP",
            _("complete"),
        )
        CANCELLED = "CN", _("cancelled")

    user = models.ForeignKey(
        usermodels.User, on_delete=models.CASCADE, related_name="orders"
    )
    ordered = models.BooleanField(default=False)
    status = models.CharField(
        max_length=3, choices=Order_Status.choices, default=Order_Status.DRAFT
    )
    delivery_cost = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_address = models.ForeignKey(usermodels.Address, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)


class OrderItem(base_models.BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="orderItem")
    inventory = models.ForeignKey(
        Inventory, on_delete=models.CASCADE, related_name="order_inventory"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
