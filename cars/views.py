from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from cars.models import Vehicle
from cars.serializers import VehicleSerializer


@api_view(['GET'])
def vehicle_list(request, format=None):
    queryset = Vehicle.objects.none()

    if request.method == 'GET':
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)