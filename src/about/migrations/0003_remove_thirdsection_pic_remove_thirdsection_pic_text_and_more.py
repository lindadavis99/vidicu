# Generated by Django 4.1 on 2022-10-01 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_secsection_delete_secondsection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thirdsection',
            name='pic',
        ),
        migrations.RemoveField(
            model_name='thirdsection',
            name='pic_text',
        ),
        migrations.AddField(
            model_name='thirdsection',
            name='pic1',
            field=models.ImageField(null=True, upload_to='about_pic/pics/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='thirdsection',
            name='pic1_text',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='thirdsection',
            name='pic2',
            field=models.ImageField(null=True, upload_to='about_pic/pics/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='thirdsection',
            name='pic2_text',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='thirdsection',
            name='pic3',
            field=models.ImageField(null=True, upload_to='about_pic/pics/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='thirdsection',
            name='pic3_text',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='thirdsection',
            name='pic4',
            field=models.ImageField(null=True, upload_to='about_pic/pics/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='thirdsection',
            name='pic4_text',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='thirdsection',
            name='pic5',
            field=models.ImageField(null=True, upload_to='about_pic/pics/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='thirdsection',
            name='pic5_text',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]