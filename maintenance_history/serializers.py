from django.forms import widgets
from rest_framework import serializers
from maintenance_history.models import MaintenanceItem, MaintenanceType


class MaintenanceItemSerializer(serializers.ModelSerializer):
    type = serializers.StringRelatedField()

    class Meta:
        model = MaintenanceItem
        fields = ('id', 'summary', 'type', 'performed_date')
