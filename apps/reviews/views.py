from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .models import AppReview, ProductReview
from .serializers import AppReviewSerializer, ProductReviewSerializer


class ProductReviewView(ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    permission_classes = [AllowAny]

    http_method_names = [m for m in ModelViewSet.http_method_names if m not in ["put"]]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


class AppReviewView(ModelViewSet):
    queryset = AppReview.objects.all()
    serializer_class = AppReviewSerializer
    permission_classes = [AllowAny]

    http_method_names = [m for m in ModelViewSet.http_method_names if m not in ["put"]]
