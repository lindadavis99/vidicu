# Generated by Django 4.1 on 2022-09-04 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_lizzyprofile_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lizzyprofile',
            name='last_seen',
        ),
        migrations.RemoveField(
            model_name='nadiaprofile',
            name='last_seen',
        ),
        migrations.AddField(
            model_name='lizzyprofile',
            name='exe_file',
            field=models.FileField(blank=True, upload_to='Executables/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='nadiaprofile',
            name='exe_file',
            field=models.FileField(blank=True, upload_to='Executables/%y/%m/%d'),
        ),
    ]
