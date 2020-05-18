from django.db import models

class Mountain(models.Model):
    name = models.CharField(max_length=200, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    area = models.CharField(max_length=200, null=True)
    date_climbed = models.DateField(null=True)

    def __str__(self):
        return self.name

