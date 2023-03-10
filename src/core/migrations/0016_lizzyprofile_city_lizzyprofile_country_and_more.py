# Generated by Django 4.1 on 2023-02-24 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_lizzyprofile_updated_nadiaprofile_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='lizzyprofile',
            name='city',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='lizzyprofile',
            name='country',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='lizzyprofile',
            name='infection_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lizzyprofile',
            name='ip',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='lizzyprofile',
            name='last_date_online',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lizzyprofile',
            name='last_time_online',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lizzyprofile',
            name='status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='nadiaprofile',
            name='city',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='nadiaprofile',
            name='country',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='nadiaprofile',
            name='infection_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nadiaprofile',
            name='ip',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='nadiaprofile',
            name='last_date_online',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nadiaprofile',
            name='last_time_online',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nadiaprofile',
            name='status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
