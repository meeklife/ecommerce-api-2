from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common import models as base_models
from apps.finance.models import Transaction
from apps.inventory.models import Inventory
from apps.users import models as usermodels


class Order(base_models.BaseModel):
    class Order_Status(models.TextChoices):
        DRAFT = "D", _("Draft"),
        PENDING = "PE", _("Pending"),
        PAYMENT_COMPLETE = "PC", _("Payment Complete"),
        IN_DELIVERY = "IND", _("in-delivery"),
        COMPLETE = "CP", _("complete"),
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
    order_date = models.DateTimeField(auto_now_add=True)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} placed an order"


class OrderItem(base_models.BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="orderItem")
    inventory = models.ForeignKey(
        Inventory, on_delete=models.CASCADE, related_name="order_inventory"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
