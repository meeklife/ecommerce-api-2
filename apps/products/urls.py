from rest_framework.routers import DefaultRouter

from .views import FavoriteView, ProductCategoryView, ProductImageView, ProductView

router = DefaultRouter()

router.register("category", ProductCategoryView, basename="category")
router.register("image", ProductImageView, basename="image")
router.register("favorite", FavoriteView, basename="favorite")
router.register("", ProductView, basename="products")

urlpatterns = router.urls
