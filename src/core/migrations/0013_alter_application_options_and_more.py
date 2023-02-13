# Generated by Django 4.1 on 2023-02-10 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_downloadpagearticle'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'ordering': ('-created',), 'verbose_name_plural': 'Application Executable'},
        ),
        migrations.RemoveField(
            model_name='application',
            name='mac_exe_file',
        ),
        migrations.AddField(
            model_name='application',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
