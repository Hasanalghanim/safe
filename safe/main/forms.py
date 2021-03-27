from django import forms
from django.forms import ModelForm
from .models import walkrequest


class walkrequestform(forms.ModelForm):
    class Meta:
        model = walkrequest
        fields = '__all__'
