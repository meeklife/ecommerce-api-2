from django.urls.conf import include, path

app_name = "api"

urlpatterns = [
    path("brands/", include("apps.brands.urls")),
    path("products/", include("apps.products.urls")),
    path("", include("apps.reviews.urls")),
    path("", include("apps.users.urls")),
]
