from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class PbsInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pbs_name = models.CharField(max_length=50, blank=True, null=True)
    pbs_name_benglai = models.CharField(max_length=50,blank=True, null=True)
    pbs_code = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    mobile_no = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.pbs_name
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
    meter_no = models.CharField(max_length=100, blank=True, null=True)
    month=models.CharField(max_length=100,blank=True, null=True)
    year=models.CharField(max_length=100,blank=True, null=True)
    pbs_code=models.CharField(max_length=100,blank=True, null=True)


    def __str__(self):
        return str(self.current3)

class MeterDataReadFinal(models.Model):
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
    meter_no = models.CharField(max_length=100, blank=True, null=True)
    month=models.IntegerField(blank=True, null=True)
    year=models.IntegerField(blank=True, null=True)
    pbs_code=models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return str(self.current3)
