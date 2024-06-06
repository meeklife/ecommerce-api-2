from rest_framework.routers import DefaultRouter

from .views import InvitationCreateListView

router = DefaultRouter()

router.register(r"", InvitationCreateListView, basename="invitation")

urlpatterns = router.urls
