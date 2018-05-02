from rest_framework import viewsets

from .models import Sessao
from .serializers import SessaoModelSerializer


class SessaoModelViewSet(viewsets.ModelViewSet):
    queryset = Sessao.objects.all()
    serializer_class = SessaoModelSerializer
