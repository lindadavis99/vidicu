# Generated by Django 4.1 on 2022-10-23 02:20

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0003_pricingfaq'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricingfaq',
            name='answer_5',
            field=tinymce.models.HTMLField(null=True),
        ),
        migrations.AddField(
            model_name='pricingfaq',
            name='answer_6',
            field=tinymce.models.HTMLField(null=True),
        ),
        migrations.AddField(
            model_name='pricingfaq',
            name='question_5',
            field=models.CharField(max_length=4000, null=True),
        ),
        migrations.AddField(
            model_name='pricingfaq',
            name='question_6',
            field=models.CharField(max_length=4000, null=True),
        ),
    ]