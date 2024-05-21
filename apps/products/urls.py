from rest_framework.routers import DefaultRouter

from .views import ProductCategoryView

router = DefaultRouter()

router.register("category", ProductCategoryView, basename="category")

urlpatterns = router.urls
