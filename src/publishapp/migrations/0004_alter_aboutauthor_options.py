# Generated by Django 4.1 on 2022-11-06 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publishapp', '0003_remove_posts_author_fullname_aboutauthor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutauthor',
            options={'verbose_name_plural': 'About Author'},
        ),
    ]
