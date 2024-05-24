from django.db import models

from apps.common import models as base_models

from ..brands.models import Brand
from ..users.models import User


class ProductCategory(base_models.BaseModel):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ("created_at",)

    def __str__(self):
        return self.name


class Products(base_models.BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    specification = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    class Meta:
        ordering = (
            "is_active",
            "updated_at",
            "created_at",
        )

    def __str__(self):
        return self.name


class ProductImage(base_models.BaseModel):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to="profile")

    class Meta:
        ordering = ("created_at",)


class Favorite(base_models.BaseModel):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ("created_at",)

    def __str__(self):
        return f"{self.user} added {self.product} to favorites"
