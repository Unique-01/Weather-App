from django import forms
from .models import *

class CityForm(forms.ModelForm):
    class Meta:
        model= City
        fields = ['title']
        widgets = {
            'title':forms.TextInput(attrs={'class':'input','placeholder': 'City Name'})
        }