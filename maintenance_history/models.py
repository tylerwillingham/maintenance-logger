from django.db import models


class MaintenanceType(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name