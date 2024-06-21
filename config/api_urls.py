from django.urls.conf import include, path

app_name = "api"

urlpatterns = [
    path("brands/", include("apps.brands.urls")),
    path("products/", include("apps.products.urls")),
    path("review/", include("apps.reviews.urls")),
    path("invitation/", include("apps.invite.urls")),
    path("inventory/", include("apps.inventory.urls")),
    path("order/", include("apps.orders.urls")),
    path("transactions/", include("apps.finance.urls")),
    path("cart/", include("apps.cart.urls")),
    path("", include("apps.users.urls")),
]
