from rest_framework.viewsets import ModelViewSet

from .models import Transaction
from .serializers import TransactionSerializer


class Transactions(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    http_method_names = [m for m in ModelViewSet.http_method_names if m not in ["put"]]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
