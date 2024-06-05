from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import Transaction
from .serializers import TransactionSerializer


class Transactions(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
