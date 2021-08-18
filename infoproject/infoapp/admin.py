from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin



# class MeterDataReadFinalAdmin(admin.ModelAdmin):
#     list_display = ('id', 'date_time_date','kvah', 'hex','current1', 'current2', 'current3','meter_no','month','year','pbs_code')
# # Register your models here.
# @admin.register(MeterDataRead)
# class MeterDataReadadmin(ImportExportModelAdmin):
#     list_display = ('id', 'date_time_date','kvah', 'hex','current1', 'current2', 'current3','meter_no','month','year','pbs_code')


admin.site.register(MeterDataReadFinal)
admin.site.register(PbsInfo)
admin.site.register(Month)
admin.site.register(Year)
admin.site.register(MeterDataRead)
