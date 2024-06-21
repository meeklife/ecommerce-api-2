from django.db import models
from apps.common import models as base_models
from apps.users.models import User
from apps.products.models import Product


class ShoppingCart(base_models.BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} Cart"


class CartItem(base_models.BaseModel):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cartproduct")
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
