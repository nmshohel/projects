# Generated by Django 3.2.6 on 2021-08-12 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meterdataread',
            name='feeder',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='meterdataread',
            name='month',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='meterdataread',
            name='substation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='meterdataread',
            name='year',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]