from django.db import models

from apps.common import models as base_models

from ..products.models import Products


class Inventory(base_models.BaseModel):
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="inventory"
    )
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
