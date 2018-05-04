from rest_framework import viewsets

from .models import Session
from .serializers import SessionSerializer


class SessionModelViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, entity=self.request.user.entity)
