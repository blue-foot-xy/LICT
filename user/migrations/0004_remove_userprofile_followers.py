# Generated by Django 3.2.4 on 2021-06-15 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_pofile_pic_userprofile_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='followers',
        ),
    ]