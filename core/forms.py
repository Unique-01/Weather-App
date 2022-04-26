from django import forms
from .models import *


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['cityname']
        widgets = {
            'cityname': forms.TextInput(attrs={'class': 'input', 'placeholder': 'City Name'})
        }
