from rest_framework.routers import DefaultRouter

from apps.cart.views import ShoppingCartViewSet

router = DefaultRouter()

# router.register("item/", CartItemViewSet, basename="Cart_Item")
router.register("", ShoppingCartViewSet, basename="Shopping_cart")


urlpatterns = router.urls
