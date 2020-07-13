from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Mountain, Hike

class DateInput(forms.DateInput):
    input_type = 'date'

class MountainForm(ModelForm):
    class Meta:
        model = Mountain
        fields = '__all__'
        widgets = {
            'date_climbed': DateInput(),
        }

class HikeForm(ModelForm):
    class Meta:
        model = Hike
        fields = '__all__'
        widgets = {
            'hike_date': DateInput(),
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']