from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common import models as base_models
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
    order = models.OneToOneField("orders.Order", on_delete=models.CASCADE)
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

    def __str__(self):
        return f"{self.user.username} made a transaction of {self.amount}"

    class Meta:
        ordering = ("created_at",)
