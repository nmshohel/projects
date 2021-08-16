from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin



# class MeterDataReadadmin(admin.ModelAdmin):
#     list_display = ('id', 'date_timee', 'pbs_code', 'month', 'year', 'current')
# Register your models here.
@admin.register(MeterDataRead)
class MeterDataReadadmin(ImportExportModelAdmin):
    list_display = ('id', 'date_time_date', 'hex','kwh', 'kwh2', 'kvarh','kvarh2', 'kvah', 'hex','current1', 'current2', 'current3')


admin.site.register(MeterDataReadFinal)
admin.site.register(PbsInfo)
