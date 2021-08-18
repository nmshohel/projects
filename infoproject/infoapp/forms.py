from django import forms
from .models import *
from django.core import validators
from django.forms import ModelForm
from django.contrib.auth.models import User


class PersonData(forms.Form):
    class meta:
        model = MeterDataRead
        fields = '__all__'

class MeterDataReadForm(forms.ModelForm):
    # month = forms.ModelChoiceField(label='মাস', widget=forms.Select(
    #     attrs={'class': 'form form-control bg-light col-md-6', }), queryset=Month.objects.all())
    # year = forms.ModelChoiceField(label='বছর', widget=forms.Select(
    #     attrs={'class': 'form form-control bg-light col-md-6', }), queryset=Year.objects.all())

    class Meta:
        model = MeterDataRead
        fields = ['sub_station_name', 'month', 'year', 'feeder_no']

        widgets = {
            'feeder_no': forms.NumberInput(attrs={'class': 'form form-control bg-light'}),
            'sub_station_name': forms.TextInput(attrs={'class': 'form form-control bg-light'}),
            'month': forms.NumberInput(attrs={'class': 'form form-control bg-light'}),
            'year': forms.NumberInput(attrs={'class': 'form form-control bg-light'}),
        }
  
