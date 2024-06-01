from django.contrib import admin

from .models import Favorite, Product, ProductCategory, ProductImage

# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Favorite)
