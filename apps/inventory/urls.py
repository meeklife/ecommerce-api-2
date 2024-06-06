from rest_framework.routers import DefaultRouter

from .views import InventoryView

router = DefaultRouter()

router.register("product", InventoryView, basename="inventory")

urlpatterns = router.urls
