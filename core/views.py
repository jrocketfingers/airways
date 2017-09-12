from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from core.models import Flight
from core.serializers import FlightSerializer


class FlightViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Flight.objects.all()
        serializer = FlightSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Flight.objects.all()
        flight = get_object_or_404(queryset, pk=pk)
        serializer = FlightSerializer(flight)
        return Response(serializer.data)
