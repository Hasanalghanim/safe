from django import forms
from django.forms import ModelForm
from .models import walkrequest


class walkrequestform(forms.ModelForm):
    class Meta:
        model = walkrequest
        fields = '__all__'

    completed = forms.BooleanField(required=False)

    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'validate'}))
    phone = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': 'validate'}))
    fromlocation = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'validate'}))
    tolocation = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'validate'}))
    timerecived = forms.DateTimeField(widget=forms.TextInput(
        attrs={'class': 'validate'}))
