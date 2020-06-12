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
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    area = models.CharField(max_length=200, null=True, choices=AREAS)
    date_climbed = models.DateField(null=True)
    notes = models.TextField(max_length=400, null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.featured_image.url
        except:
            url = ''
        return url

class Hike(models.Model):
    name = models.CharField(max_length=200, null=True)
    length = models.DecimalField('Length (km)', max_digits=6, decimal_places=2, null=True)
    duration = models.CharField('Duration (hh:mm:ss)', max_length=200, null=True)
    total_ascent = models.DecimalField('Total Ascent (m)', max_digits=6, decimal_places=2, null=True)
    total_descent = models.DecimalField('Total Decsent (m)', max_digits=6, decimal_places=2, null=True)
    hike_date = models.DateField(null=True)
    notes = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.length} km'
    
    @property
    def imageURL(self):
        try:
            url = self.featured_image.url
        except:
            url = ''
        return url

class Image(models.Model):
    hike = models.ForeignKey(Hike, on_delete=models.CASCADE)
    image = models.ImageField()

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        print('URL', url)
        return url

class MountainImage(models.Model):
    peak = models.ForeignKey(Mountain, on_delete=models.CASCADE)
    image = models.ImageField()

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        print('URL', url)
        return url
