from rest_framework import serializers

from .models import Sessao


class SessaoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sessao
        fields = ('numero', 'data', 'inicio', 'fim')
