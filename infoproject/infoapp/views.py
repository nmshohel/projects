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
    return redirect('user-login')

def home_page(request):
    return render(request, 'home_page.html')

def delete_page(request):
    return render(request, 'data-delete.html')

    

def view_result(request):
    return render(request, 'result.html')

def meter_data_calculation(request):
    month=request.POST.get('month')
    year=request.POST.get('year')
    current_user = request.user
    user_id = current_user.id
    user_pbs_info = PbsInfo.objects.get(user__pk=user_id)
    pbs_code=user_pbs_info.pbs_code
    count = 0
    duration = 0
    print(month)
    print(year)
    print(pbs_code)
    data = MeterDataReadFinal.objects.filter(pbs_code=pbs_code,month=month,year=year)
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

    return render(request, 'monthly-result.html',context)


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
        # return render(request, 'meter-info.html')
        

    context={'msg2':msg2}
    return render(request, 'upload.html',context)

# def meter_info(request):
#     month=request.POST.get('month')
#     year=request.POST.get('year')
#     current_user = request.user
#     user_id = current_user.id
#     user_pbs_info = PbsInfo.objects.get(user__pk=user_id)
#     print(user_pbs_info.pbs_code)
#     pbs_code=user_pbs_info.pbs_code
#     MeterDataRead.objects.all().update(month=month, year=year,pbs_code=pbs_code)
#     data=MeterDataRead.objects.filter(month=month, year=year, pbs_code=pbs_code)
#     for data in data:
#         MeterDataReadFinal.objects.create(date_time_date=data.date_time_date,hex=data.hex,kwh=data.kwh,
#         kwh2=data.kwh2,kvarh=data.kvarh,kvarh2=data.kvarh2,kvah=data.kvah,avah2=data.avah2,voltage1=data.voltage1,
#         voltage2=data.voltage2,voltage3=data.voltage3,current1=data.current1,current2=data.current2,current3=data.current3,
#          month=data.month, year=data.year,pbs_code=data.pbs_code)
  
#     return render(request, 'meter-info.html')
def meter_info(request):
    if request.method == 'POST':
        current_user = request.user
        user_id = current_user.id
        user_pbs_info = PbsInfo.objects.get(user__pk=user_id)
        pbs_code=user_pbs_info.pbs_code
        month_id = request.POST['month']
        year_id = request.POST['year']
        month = Month.objects.get(id=month_id)
        year = Year.objects.get(id=year_id)
        
        # month = request.POST.get('month')
        # year = request.POST.get('year')
        feeder_no_id = request.POST.get('feeder_no')
        sub_station_name_id = request.POST.get('sub_station_name')
        print("substation id",sub_station_name_id)
        feeder_no = Feeder.objects.get(id=feeder_no_id)
        sub_station_name = Substation.objects.filter(pbs_code=pbs_code)
        sub_station_name=str(sub_station_name)
        feeder_no=str(feeder_no)
        month=str(month)
        year=str(year)
        MeterDataRead.objects.all().update(month=month, year=year,pbs_code=pbs_code,feeder_no=feeder_no,sub_station_name=sub_station_name)
        data=MeterDataRead.objects.filter(month=month, year=year, pbs_code=pbs_code,feeder_no=feeder_no,sub_station_name=sub_station_name)
        for data in data:
            MeterDataReadFinal.objects.create(date_time_date=data.date_time_date,hex=data.hex,kwh=data.kwh,
            kwh2=data.kwh2,kvarh=data.kvarh,kvarh2=data.kvarh2,kvah=data.kvah,avah2=data.avah2,voltage1=data.voltage1,
            voltage2=data.voltage2,voltage3=data.voltage3,current1=data.current1,current2=data.current2,current3=data.current3,
            month=data.month, year=data.year,pbs_code=data.pbs_code,sub_station_name=data.sub_station_name,feeder_no=feeder_no)

        data_form = MeterDataReadForm()
        message = "Information Successfully Added!"
        context = {'data_form': data_form, 'message': message}
        # return render(request, 'meter-info.html', context)
        return redirect('/data-delete')
    else:
        data_form = MeterDataReadForm()
        context = {'data_form': data_form}
        return render(request, 'meter-info.html', context)

def data_delete(request):
    delete_data = MeterDataRead.objects.all()
    delete_data.delete()
    # MeterDataReadFinal.objects.all().delete()
    msg="Data Successfully Deleted"
    context={'msg':msg}
    # return render(request, 'data-delete.html',context)
    # return render(request, 'upload.html',context)
    return redirect('/')
    # return HttpResponse("Uploded")

