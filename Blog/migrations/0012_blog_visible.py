# Generated by Django 5.0.1 on 2024-02-03 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0011_theme_blog_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='visible',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]