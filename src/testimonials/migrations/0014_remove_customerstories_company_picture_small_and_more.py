# Generated by Django 4.1 on 2023-02-10 00:08

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0013_blockquote_quote_alter_blockquote_company_logo_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerstories',
            name='company_picture_small',
        ),
        migrations.AlterField(
            model_name='customerstories',
            name='company_logo',
            field=imagekit.models.fields.ProcessedImageField(upload_to='Customerstories/companylogo/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='customerstories',
            name='company_picture_large',
            field=imagekit.models.fields.ProcessedImageField(upload_to='Customerstories/%y/%m/%d'),
        ),
    ]