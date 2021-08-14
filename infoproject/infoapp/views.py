from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.db import models
from infoapp.models import *
from infoapp.forms import *
# from django import bangla
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
import random


from .resources import PersonResource
from tablib import Dataset
# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST['uname1']
        password = request.POST['pwd1']
        user=authenticate(username=username, password=password)
        if(user):
            login(request, user)
            return redirect('/home-page')
    return render(request, 'user_login.html')
def user_logout(request):
    logout(request)
    return redirect('/')

def home_page(request):
    return render(request, 'home_page.html')

def delete_page(request):
    return render(request, 'data-delete.html')

    

def view_result(request):
    return render(request, 'result.html')

def meter_data_calculation(request):
    count = 0
    duration = 0
    data = MeterDataRead.objects.all()
    datalist = []
    for item in data:
        datalist.append(item.current3)
    f = True
    for x in datalist:
        if x == '0':
            if f:
                count = count+1
            f = False
            duration = duration+5
        else:
            f = True
    context={'count':count,'duration':duration}

    return render(request, 'result.html',context)


def simple_upload(request):
    msg2=""
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']
        # month = request.POST['month']
        # year = request.POST['year']
        # substation = request.POST['substation']
        # feeder = request.POST['feeder']
        # print(month)
        # print(year)
        # print(substation)
        # print(feeder)
        # MeterDataRead.objects.create(month=month, year=year,substation=substation,feeder=feeder)
        imported_data = dataset.load(new_persons.read(), format='xlsx')
        # print(imported_data)
        for data in imported_data:
            value = MeterDataRead(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
                data[11],
                data[12],
                data[13],
                data[14],
            )
            value.save()
            msg2="Data Successfully Uploded"

    
    
    context={'msg2':msg2}
    return render(request, 'upload.html',context)

def data_delete(request):
    data = MeterDataRead.objects.all()
    data.delete()
    msg="Data Successfully Deleted"
    context={'msg':msg}
    return render(request, 'data-delete.html',context)

