# Generated by Django 5.0.4 on 2024-06-10 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EducationApi', '0003_videos_remove_courses_author_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='image',
            field=models.ImageField(default='pngwing.com.png', upload_to='images'),
        ),
    ]
