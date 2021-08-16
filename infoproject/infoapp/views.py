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

        return redirect('/meter-info')
        

    context={'msg2':msg2}
    return render(request, 'upload.html',context)

def meter_info(request):
    meter_no=request.POST.get('m_no')
    month=request.POST.get('month')
    year=request.POST.get('year')
    # print(month)
    # print(year)
    # print(meter_no)
    # user=request.user
    # print(user)
    # PbsInfo.objects.get()
    current_user = request.user
    user_id = current_user.id
    user_pbs_info = PbsInfo.objects.get(user__pk=user_id)
    print(user_pbs_info.pbs_code)
    pbs_code=user_pbs_info.pbs_code
    MeterDataRead.objects.all().update(meter_no=meter_no,month=month, year=year,pbs_code=pbs_code)
    data=MeterDataRead.objects.filter(meter_no=100111)
    for data in data:
        MeterDataReadFinal.objects.create(date_time_date=data.date_time_date,hex=data.hex,kwh=data.kwh,
        kwh2=data.kwh2,kvarh=data.kvarh,kvarh2=data.kvarh2,kvah=data.kvah,avah2=data.avah2,voltage1=data.voltage1,
        voltage2=data.voltage2,voltage3=data.voltage3,current1=data.current1,current2=data.current2,current3=data.current3,
        meter_no=data.meter_no, month=data.month, year=data.year,pbs_code=data.pbs_code)
    
    return render(request, 'meter-info.html')

def data_delete(request):
    data = MeterDataRead.objects.all()
    data.delete()
    msg="Data Successfully Deleted"
    context={'msg':msg}
    return render(request, 'data-delete.html',context)

