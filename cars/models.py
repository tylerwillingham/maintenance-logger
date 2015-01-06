from django.db import models


class Car(models.Model):
    title = models.CharField(max_length=60)
    vin = models.CharField(max_length=100)
    purchase_date = models.DateField()
    sale_date = models.DateField()
    year = models.CharField(max_length=4)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    bodystyle = models.CharField(max_length=16)

    def __str__(self):
        return self.title