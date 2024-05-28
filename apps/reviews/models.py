from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from apps.common import models as base_models

from ..products.models import Products
from ..users.models import User


class ProductReview(base_models.BaseModel):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    description = models.TextField(blank=True)
