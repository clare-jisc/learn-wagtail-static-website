# Generated by Django 5.0.6 on 2024-05-23 06:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0002_rename_footerlinks_socialmedialinks'),
        ('wagtailimages', '0026_delete_uploadedimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogoSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]