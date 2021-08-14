from django import forms
from .models import *
from django.core import validators
from django.forms import ModelForm
from django.contrib.auth.models import User


class PersonData(forms.Form):
    class meta:
        model = MeterDataRead
        fields = '__all__'

