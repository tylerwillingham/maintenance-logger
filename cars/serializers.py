from django.forms import widgets
from rest_framework import serializers
from cars.models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id', 'title', 'vin', 'purchase_date', 'sale_date', 'year', 'make', 'model', 'bodystyle')