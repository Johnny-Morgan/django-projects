from django.contrib import admin

from .models import Mountain, Hike, Image, MountainImage

admin.site.register(Mountain)
admin.site.register(Hike)
admin.site.register(Image)
admin.site.register(MountainImage)
