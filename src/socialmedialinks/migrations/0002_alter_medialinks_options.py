# Generated by Django 4.1 on 2023-02-08 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedialinks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medialinks',
            options={'ordering': ('created',), 'verbose_name_plural': 'MediaLinks'},
        ),
    ]
