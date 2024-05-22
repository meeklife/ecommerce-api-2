from django.db import models

from apps.common import models as base_models

from ..brands.models import Brand


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
