# Generated by Django 5.0.6 on 2024-05-24 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_homepage_cta_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='my_story_content',
            field=models.TextField(blank=True, default='', max_length=500),
        ),
        migrations.AddField(
            model_name='homepage',
            name='my_story_title',
            field=models.CharField(blank=True, default='My Story', max_length=40),
        ),
    ]
