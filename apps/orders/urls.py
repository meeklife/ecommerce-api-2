from rest_framework.routers import DefaultRouter

from .views import OrderItems, Orders, Transactions

router = DefaultRouter()

router.register("transcation", Transactions, basename="order_transaction")
router.register("item", OrderItems, basename="order_item")
router.register("", Orders, basename="order")

urlpatterns = router.urls
