from django.forms import widgets
from rest_framework import serializers
from cars.models import Vehicle
from maintenance_history.serializers import MaintenanceItemSerializer


class VehicleSerializer(serializers.ModelSerializer):
    maintenance = MaintenanceItemSerializer(many=True, read_only=True)

    class Meta:
        model = Vehicle
        fields = ('id', 'title', 'vin', 'purchase_date', 'sale_date', 'year', 'make', 'model', 'bodystyle', 'maintenance')
