# Generated by Django 4.1 on 2022-10-23 02:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pricing', '0002_delete_pricingfaq'),
    ]

    operations = [
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
    ]