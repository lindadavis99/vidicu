# Generated by Django 4.1 on 2022-10-23 02:06

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
            name='TeamsPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_heading', models.CharField(max_length=1000)),
                ('pricing', models.DecimalField(decimal_places=4, max_digits=8)),
                ('feature_1', models.CharField(max_length=1000)),
                ('feature_2', models.CharField(max_length=1000)),
                ('feature_3', models.CharField(max_length=1000)),
                ('feature_4', models.CharField(max_length=1000)),
                ('feature_5', models.CharField(max_length=1000)),
                ('feature_6', models.CharField(max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='ProfessionalPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_heading', models.CharField(max_length=1000)),
                ('pricing', models.DecimalField(decimal_places=4, max_digits=8)),
                ('feature_1', models.CharField(max_length=1000)),
                ('feature_2', models.CharField(max_length=1000)),
                ('feature_3', models.CharField(max_length=1000)),
                ('feature_4', models.CharField(max_length=1000)),
                ('feature_5', models.CharField(max_length=1000)),
                ('feature_6', models.CharField(max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='PricingHeading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=1000)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PricingFAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_1', models.CharField(max_length=4000)),
                ('answer_1', tinymce.models.HTMLField()),
                ('question_2', models.CharField(max_length=4000)),
                ('answer_2', tinymce.models.HTMLField()),
                ('question_3', models.CharField(max_length=4000)),
                ('answer_3', tinymce.models.HTMLField()),
                ('question_4', models.CharField(max_length=4000)),
                ('answer_4', tinymce.models.HTMLField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='PricingComparePlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(max_length=1000, null=True)),
                ('professional', models.BooleanField(default=False)),
                ('teams', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='HighLightSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=4000)),
                ('testimonial', models.CharField(max_length=1000)),
                ('user_full_name', models.CharField(max_length=1000)),
                ('user_pic', models.ImageField(blank=True, null=True, upload_to='Pricing/images/%y/%m/%d')),
                ('user_title', models.CharField(max_length=1000)),
                ('first_status', models.CharField(max_length=1000)),
                ('first_status_desc', models.CharField(max_length=1000)),
                ('second_status', models.CharField(max_length=1000)),
                ('second_status_desc', models.CharField(max_length=1000)),
                ('third_status', models.CharField(max_length=1000)),
                ('third_status_desc', models.CharField(max_length=1000)),
                ('fourth_status', models.CharField(max_length=1000)),
                ('fourth_status_desc', models.CharField(max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
