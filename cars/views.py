from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cars.models import Vehicle
from cars.serializers import VehicleSerializer
from django.contrib.auth.models import User
from django.http import Http404


@api_view(['GET'])
def vehicle_list(request, username, format=None):
    try:
        user = User.objects.get(username=username)
    except Vehicle.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        vehicles = Vehicle.objects.filter(owner=user, sale_date__isnull=True)
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)