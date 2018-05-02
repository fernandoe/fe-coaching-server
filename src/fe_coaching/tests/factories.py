import factory
from django.contrib.auth import get_user_model

from ..models import Sessao

User = get_user_model()


class SessaoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Sessao
