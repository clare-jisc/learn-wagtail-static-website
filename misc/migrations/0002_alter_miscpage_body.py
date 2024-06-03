# Generated by Django 5.0.6 on 2024-06-03 10:00

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('misc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miscpage',
            name='body',
            field=wagtail.fields.StreamField([('content', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'ol', 'ul', 'hr', 'h3'], template='blocks/richtext.html')), ('image', wagtail.images.blocks.ImageChooserBlock(template='blocks/image.html'))]),
        ),
    ]