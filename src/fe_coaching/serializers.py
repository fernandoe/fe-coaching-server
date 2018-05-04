from rest_framework import serializers

from .models import Session


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        read_only_fields = ('uuid',)
        fields = ('uuid', 'created_at', 'updated_at', 'number', 'date', 'start', 'end')
