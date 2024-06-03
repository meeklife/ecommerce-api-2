from rest_framework.routers import DefaultRouter

from .views import OrderItems, Orders

router = DefaultRouter()


router.register("item", OrderItems, basename="order_item")
router.register("", Orders, basename="order")

urlpatterns = router.urls
