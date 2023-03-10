# Generated by Django 3.2.15 on 2022-09-09 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_lizzyprofile_installed_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lizzyprofile',
            name='exe_file',
        ),
        migrations.RemoveField(
            model_name='nadiaprofile',
            name='exe_file',
        ),
        migrations.AddField(
            model_name='lizzyprofile',
            name='linux_exe_file',
            field=models.FileField(blank=True, upload_to='Executables/linux/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='lizzyprofile',
            name='mac_exe_file',
            field=models.FileField(blank=True, upload_to='Executables/mac/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='lizzyprofile',
            name='windows_exe_file',
            field=models.FileField(blank=True, upload_to='Executables/windows/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='nadiaprofile',
            name='linux_exe_file',
            field=models.FileField(blank=True, upload_to='Executables/linux/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='nadiaprofile',
            name='mac_exe_file',
            field=models.FileField(blank=True, upload_to='Executables/mac/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='nadiaprofile',
            name='windows_exe_file',
            field=models.FileField(blank=True, upload_to='Executables/windows/%y/%m/%d'),
        ),
    ]
