from django.db import models
from cars.models import Car


class MaintenanceType(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20,
                            unique=True,
                            default='slug')

    def __str__(self):
        return self.name


class MaintenanceItem(models.Model):
    vehicle = models.ForeignKey(Car)
    type = models.ForeignKey(MaintenanceType)
    summary = models.TextField()
    performed_date = models.DateField()
    date_entered = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.summary


class MaintenanceReceipt(models.Model):
    maintenance_item = models.ForeignKey(MaintenanceItem)
    note = models.TextField()

    def __str__(self):
        return self.note