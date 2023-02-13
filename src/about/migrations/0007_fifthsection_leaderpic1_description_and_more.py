# Generated by Django 4.1 on 2023-02-08 09:56

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_delete_thirdsection'),
    ]

    operations = [
        migrations.AddField(
            model_name='fifthsection',
            name='leaderpic1_description',
            field=models.CharField(default='Image Description', max_length=500),
        ),
        migrations.AddField(
            model_name='fifthsection',
            name='leaderpic2_description',
            field=models.CharField(default='Image Description', max_length=500),
        ),
        migrations.AddField(
            model_name='fifthsection',
            name='leaderpic3_description',
            field=models.CharField(default='Image Description', max_length=500),
        ),
        migrations.AlterField(
            model_name='fifthsection',
            name='leaderpic1',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='about_pic/leadership/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='fifthsection',
            name='leaderpic2',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='about_pic/leadership/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='fifthsection',
            name='leaderpic3',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='about_pic/leadership/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='firstsection',
            name='about_pic',
            field=imagekit.models.fields.ProcessedImageField(upload_to='about_pic/%y/%m/%d'),
        ),
    ]
