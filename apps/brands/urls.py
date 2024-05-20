from rest_framework.routers import DefaultRouter

from .views import BrandView

router = DefaultRouter()

router.register("", BrandView, basename="brand")

urlpatterns = router.urls
