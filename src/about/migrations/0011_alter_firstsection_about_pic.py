# Generated by Django 4.1 on 2023-02-14 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0010_alter_aboutusicons_pic1_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstsection',
            name='about_pic',
            field=models.ImageField(upload_to='about_pic/%y/%m/%d'),
        ),
    ]