from django.contrib.auth import get_user_model
from django.db import models
from fe_core.models import UUIDModel, Entity

User = get_user_model()


class Sessao(UUIDModel):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    entidade = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
    numero = models.PositiveIntegerField(null=True)
    data = models.DateField(null=True)
    inicio = models.TimeField(null=True)
    fim = models.TimeField(null=True)
    conteudo = models.TextField(null=True)
