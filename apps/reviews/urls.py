from rest_framework.routers import DefaultRouter

from .views import AppReviewView, ProductReviewView

router = DefaultRouter()

router.register("product", ProductReviewView, basename="product_review")
router.register("app", AppReviewView, basename="app_review")

urlpatterns = router.urls
