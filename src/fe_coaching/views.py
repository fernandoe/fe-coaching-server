from rest_framework import viewsets

from .models import Session
from .serializers import SessionModelSerializer


class SessionModelViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionModelSerializer
