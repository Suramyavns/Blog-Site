# Generated by Django 4.2.7 on 2023-11-24 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_blog_thumb_alter_blog_date_alter_blog_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='thumb',
            field=models.ImageField(upload_to='thumbnails'),
        ),
    ]
