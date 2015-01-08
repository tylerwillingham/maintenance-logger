from django.db import models


class Vehicle(models.Model):
    title = models.CharField(max_length=60)
    vin = models.CharField(max_length=100, blank=True)
    purchase_date = models.DateField(blank=True, null=True)
    sale_date = models.DateField(blank=True, null=True)
    year = models.CharField(max_length=4)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    bodystyle = models.CharField(max_length=16)

    def __str__(self):
        return ' '.join([self.year, self.make, self.model, self.bodystyle, 'VIN: {}'.format(self.vin)])