from rest_framework import serializers
from core.models import Flight, Company


class DefaultModelSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('created_at', 'created_by',
                   'updated_at', 'updated_by',
                   'deleted_at', 'deleted_by',)


class FlightSerializer(DefaultModelSerializer):
    class Meta(DefaultModelSerializer.Meta):
        depth = 1
        model = Flight
