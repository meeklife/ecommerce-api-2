from django.urls.conf import include, path

app_name = "api"

urlpatterns = [
    path("brands/", include("apps.brands.urls")),
    path("", include("apps.users.urls")),
]
