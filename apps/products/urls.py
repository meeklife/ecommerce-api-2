from rest_framework.routers import DefaultRouter

from .views import ProductCategoryView, ProductView

router = DefaultRouter()

router.register("category", ProductCategoryView, basename="category")
router.register("", ProductView, basename="products")

urlpatterns = router.urls
