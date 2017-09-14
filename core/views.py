from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from core.models import Flight, FlightUpdate
from core.serializers import FlightSerializer, FlightUpdateSerializer


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


class FlightUpdateViewSet(viewsets.ViewSet):
    def create(self, request, flight_pk=None, pk=None):
        data = {
            'flight_id': flight_pk,
            **request.data,
        }
        serializer = FlightUpdateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def list(self, request, flight_pk=None):
        queryset = FlightUpdate.objects.filter(flight_id=flight_pk)
        serializer = FlightUpdateSerializer(queryset, many=True)
        return Response(serializer.data)


class FlightTakeOffViewSet(viewsets.ViewSet):
    def create(self, request, flight_pk=None)
        queryset = Flight.objects.all()
        flight = get_object_or_404(queryset, pk=flight_pk)
