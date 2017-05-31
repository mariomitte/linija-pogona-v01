from django import forms
from django.contrib.auth.models import User

from .models import Operater, Pwm


class OperaterForm(forms.ModelForm):

    class Meta:
        model = Operater
        fields = ['kreirao', 'nalog', 'sifra', 'slika']

class PwmForm(forms.ModelForm):

    class Meta:
        model = Pwm
        fields = ['period', 'sirina']
