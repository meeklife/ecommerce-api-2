from django.contrib import admin

from .models import AppReview, ProductReview

# Register your models here.
admin.site.register(ProductReview)
admin.site.register(AppReview)
