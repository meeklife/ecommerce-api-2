from rest_framework.routers import DefaultRouter

from apps.orders.views import OrderItemViewset, OrderViewSet

router = DefaultRouter()

router.register("item", OrderItemViewset, basename="order_item")
router.register("", OrderViewSet, basename="order")

urlpatterns = router.urls
