# Generated by Django 5.0.1 on 2024-02-01 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_blogimage_bloglink_alter_blogcontent_image_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
