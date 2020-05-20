from django.db import models

class Mountain(models.Model):
    AREAS = (
            ('Dublin/Wicklow', 'Dublin/Wicklow'),
            ('North Midlands', 'North Midlands'),
            ('East Coast', 'East Coast'),
            ('Snowdonia', 'Snowdonia')
    )
    name = models.CharField(max_length=200, null=True)
    height = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    area = models.CharField(max_length=200, null=True, choices=AREAS)
    date_climbed = models.DateField(null=True)

    def __str__(self):
        return self.name

class Hike(models.Model):
    length = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    duration = models.CharField('Duration (hh:mm:ss)', max_length=200, null=True)
    total_ascent = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    total_descent = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    hike_date = models.DateField(null=True)
    notes = models.TextField(null=True)

    def __str__(self):
        return f'{self.length} km'