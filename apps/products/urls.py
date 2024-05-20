from rest_framework.routers import DefaultRouter

from .views import ProductCategoryView

router = DefaultRouter()

router.register("", ProductCategoryView, basename="product-category")

urlpatterns = router.urls
