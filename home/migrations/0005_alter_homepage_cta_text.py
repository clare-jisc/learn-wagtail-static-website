# Generated by Django 5.0.6 on 2024-05-23 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homepage_cta_page_homepage_cta_text_homepage_cta_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='cta_text',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
