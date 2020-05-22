from django.forms import ModelForm
from .models import Mountain


class MountainForm(ModelForm):
    class Meta:
        model = Mountain
        fields = '__all__'