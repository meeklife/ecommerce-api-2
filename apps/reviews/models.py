from django.db import models

from ..products.models import Products
from ..users.models import User

# from apps.common import models as base_models


class ProductReview(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    description = models.TextField()
