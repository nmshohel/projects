from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm



class MeterDataRead(models.Model):
    id = models.AutoField(primary_key=True)
    date_time_date = models.CharField(max_length=100, blank=True, null=True)
    hex = models.CharField(max_length=100, blank=True, null=True)
    kwh = models.CharField(max_length=100, blank=True, null=True)
    kwh2 = models.CharField(max_length=100, blank=True, null=True)
    kvarh = models.CharField(max_length=100, blank=True, null=True)
    kvarh2 = models.CharField(max_length=100, blank=True, null=True)
    kvah = models.CharField(max_length=100, blank=True, null=True)
    avah2 = models.CharField(max_length=100, blank=True, null=True)
    voltage1 = models.CharField(max_length=100, blank=True, null=True)
    voltage2 = models.CharField(max_length=100, blank=True, null=True)
    voltage3 = models.CharField(max_length=100, blank=True, null=True)
    current1 = models.CharField(max_length=100, blank=True, null=True)
    current2 = models.CharField(max_length=100, blank=True, null=True)
    current3 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.current3)
