from rest_framework.generics import CreateAPIView, ListAPIView

from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response

from rest_framework import status

from .models import Invitation

from .serializers import InvitationSerializer

class InvitationCreateListView(CreateAPIView, ListAPIView):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Handle POST requests to create a new Invitation.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


    def list(self, request, *args, **kwargs):
        """
        Handle GET requests to list existing Invitations.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
