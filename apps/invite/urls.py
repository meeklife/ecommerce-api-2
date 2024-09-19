from django.urls import path

from .views import InvitationCreateListView

urlpatterns = [
    path(r"", InvitationCreateListView.as_view(), name="invitation"),
]
