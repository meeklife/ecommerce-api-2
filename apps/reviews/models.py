from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from apps.common import models as base_models

from ..products.models import Product
from ..users.models import User


class ProductReview(base_models.BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    description = models.TextField(blank=True)

    def __str__(self):
        return (
            f"{self.user.username} gave {self.product.name} a ratings of {self.rating}"
        )


class AppReview(base_models.BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    description = models.TextField(blank=True)

    class Meta:
        ordering = ("created_at",)

    def __str__(self):
        return f"{self.user.username} gave a ratings of {self.rating}"
