# Generated by Django 4.1 on 2022-10-28 03:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerStories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('company_picture_small', models.ImageField(upload_to='Customerstories/%y/%m/%d')),
                ('company_picture_large', models.ImageField(upload_to='Customerstories/%y/%m/%d')),
                ('testimonal_title', models.CharField(max_length=4000)),
                ('body', tinymce.models.HTMLField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'CustomerStories',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='CompanyLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_logo', models.ImageField(blank=True, null=True, upload_to='Customerstories/companylogo/%y/%m/%d')),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'CustomerStories',
                'ordering': ('created',),
            },
        ),
    ]
