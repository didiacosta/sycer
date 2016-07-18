from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Usuario 

class EditarEmailForm (forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

class EditarFotoForm (ModelForm):
    foto = forms.ImageField()
    class Meta:
        model=Usuario
        fields=['foto']


