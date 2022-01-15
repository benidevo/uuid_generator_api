from rest_framework import serializers

from .models import UUIDModel


class UUIDModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UUIDModel
        fields = ('id', 'created_at')
