from rest_framework.routers import DefaultRouter

from .views import ProductReviewView

router = DefaultRouter()

router.register("product", ProductReviewView, basename="product_review")

urlpatterns = router.urls
