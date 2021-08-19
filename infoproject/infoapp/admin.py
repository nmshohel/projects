from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin



# class MeterDataReadFinalAdmin(admin.ModelAdmin):
#     list_display = ('id', 'date_time_date','kvah', 'hex','current1', 'current2', 'current3','meter_no','month','year','pbs_code')
# # Register your models here.
# @admin.register(MeterDataRead)
class MeterDataReadadmin(ImportExportModelAdmin):
     list_display = ('id', 'date_time_date','kvah','current1', 'current2', 'current3','sub_station_name','feeder_no','month','year','pbs_code')
class MeterDataReadFinaladmin(ImportExportModelAdmin):
     list_display = ('id', 'date_time_date','kvah', 'current1', 'current2', 'current3','sub_station_name','feeder_no','month','year','pbs_code')


admin.site.register(MeterDataReadFinal, MeterDataReadFinaladmin)
admin.site.register(PbsInfo)
admin.site.register(Month)
admin.site.register(Year)
admin.site.register(MeterDataRead,MeterDataReadadmin)
admin.site.register(Substation)
admin.site.register(Feeder)
