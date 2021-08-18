# Generated by Django 3.2.6 on 2021-08-18 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MeterDataRead',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date_time_date', models.CharField(blank=True, max_length=100, null=True)),
                ('hex', models.CharField(blank=True, max_length=100, null=True)),
                ('kwh', models.CharField(blank=True, max_length=100, null=True)),
                ('kwh2', models.CharField(blank=True, max_length=100, null=True)),
                ('kvarh', models.CharField(blank=True, max_length=100, null=True)),
                ('kvarh2', models.CharField(blank=True, max_length=100, null=True)),
                ('kvah', models.CharField(blank=True, max_length=100, null=True)),
                ('avah2', models.CharField(blank=True, max_length=100, null=True)),
                ('voltage1', models.CharField(blank=True, max_length=100, null=True)),
                ('voltage2', models.CharField(blank=True, max_length=100, null=True)),
                ('voltage3', models.CharField(blank=True, max_length=100, null=True)),
                ('current1', models.CharField(blank=True, max_length=100, null=True)),
                ('current2', models.CharField(blank=True, max_length=100, null=True)),
                ('current3', models.CharField(blank=True, max_length=100, null=True)),
                ('sub_station_name', models.CharField(blank=True, max_length=100, null=True)),
                ('feeder_no', models.CharField(blank=True, max_length=100, null=True)),
                ('month', models.CharField(blank=True, max_length=100, null=True)),
                ('year', models.CharField(blank=True, max_length=100, null=True)),
                ('pbs_code', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MeterDataReadFinal',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date_time_date', models.CharField(blank=True, max_length=100, null=True)),
                ('hex', models.CharField(blank=True, max_length=100, null=True)),
                ('kwh', models.CharField(blank=True, max_length=100, null=True)),
                ('kwh2', models.CharField(blank=True, max_length=100, null=True)),
                ('kvarh', models.CharField(blank=True, max_length=100, null=True)),
                ('kvarh2', models.CharField(blank=True, max_length=100, null=True)),
                ('kvah', models.CharField(blank=True, max_length=100, null=True)),
                ('avah2', models.CharField(blank=True, max_length=100, null=True)),
                ('voltage1', models.CharField(blank=True, max_length=100, null=True)),
                ('voltage2', models.CharField(blank=True, max_length=100, null=True)),
                ('voltage3', models.CharField(blank=True, max_length=100, null=True)),
                ('current1', models.CharField(blank=True, max_length=100, null=True)),
                ('current2', models.CharField(blank=True, max_length=100, null=True)),
                ('current3', models.CharField(blank=True, max_length=100, null=True)),
                ('sub_station_name', models.CharField(blank=True, max_length=100, null=True)),
                ('feeder_no', models.CharField(blank=True, max_length=100, null=True)),
                ('month', models.CharField(blank=True, max_length=100, null=True)),
                ('year', models.CharField(blank=True, max_length=100, null=True)),
                ('pbs_code', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PbsInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pbs_name', models.CharField(blank=True, max_length=50, null=True)),
                ('pbs_name_benglai', models.CharField(blank=True, max_length=50, null=True)),
                ('pbs_code', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.TextField(blank=True, max_length=50, null=True)),
                ('mobile_no', models.TextField(blank=True, max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
