# Generated by Django 4.1 on 2022-11-10 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0007_customerstories_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerstories',
            name='status',
        ),
        migrations.RemoveField(
            model_name='customerstories',
            name='tags',
        ),
    ]