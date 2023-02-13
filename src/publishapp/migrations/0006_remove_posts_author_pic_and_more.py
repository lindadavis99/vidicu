# Generated by Django 4.1 on 2023-02-08 07:55

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('publishapp', '0005_remove_posts_large_post_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='author_pic',
        ),
        migrations.AddField(
            model_name='aboutauthor',
            name='author_pic_description',
            field=models.CharField(default='Image Description', max_length=500),
        ),
        migrations.AlterField(
            model_name='aboutauthor',
            name='author_pic',
            field=imagekit.models.fields.ProcessedImageField(upload_to='AboutAuthor/%y/%m/%d'),
        ),
    ]
