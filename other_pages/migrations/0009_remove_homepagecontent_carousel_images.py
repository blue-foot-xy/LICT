# Generated by Django 3.2.4 on 2021-06-15 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('other_pages', '0008_auto_20210615_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepagecontent',
            name='carousel_images',
        ),
    ]
