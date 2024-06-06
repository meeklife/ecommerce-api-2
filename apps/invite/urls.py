from rest_framework.routers import DefaultRouter

from .views import InvitationCreateListView

router = DefaultRouter()

router.register(r"invitations", InvitationCreateListView, basename="")

urlpatterns = router.urls
