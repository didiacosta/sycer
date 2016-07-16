from django import forms
from django.contrib.auth.models import User

class EditarEmailForm (forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))


  