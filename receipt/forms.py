from django import forms
from .models import Paragon


class ParagonForm(forms.ModelForm):
    class Meta:
        model = Paragon
        fields =('image',)

