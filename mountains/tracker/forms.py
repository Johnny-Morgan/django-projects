from django.forms import ModelForm
from .models import Mountain, Hike


class MountainForm(ModelForm):
    class Meta:
        model = Mountain
        fields = '__all__'


class HikeForm(ModelForm):
    class Meta:
        model = Hike
        fields = '__all__'