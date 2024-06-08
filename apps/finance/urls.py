from rest_framework.routers import DefaultRouter

from .views import Transactions

router = DefaultRouter()

router.register("", Transactions, basename="order_transaction")

urlpatterns = router.urls
