from rest_framework import serializers

from .models import Session


class SessionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('number', 'date', 'start', 'end')
