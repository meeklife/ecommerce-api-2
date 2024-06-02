from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import AppReview, ProductReview
from .serializers import AppReviewSerializer, ProductReviewSerializer


class ProductReviewView(ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    permission_classes = [IsAuthenticated]

    http_method_names = [
        m for m in ModelViewSet.http_method_names if m not in ["put", "patch"]
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AppReviewView(ModelViewSet):
    queryset = AppReview.objects.all()
    serializer_class = AppReviewSerializer
    permission_classes = [IsAuthenticated]

    http_method_names = [
        m for m in ModelViewSet.http_method_names if m not in ["put", "patch"]
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
