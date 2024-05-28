from django.contrib import admin

from .models import Favorite, ProductCategory, ProductImage, Products

# Register your models here.
admin.register(ProductCategory)
admin.register(Products)
admin.register(ProductImage)
admin.register(Favorite)
