# Generated by Django 3.2.4 on 2021-06-15 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('other_pages', '0002_auto_20210615_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organiztion_name', models.CharField(max_length=200)),
                ('college_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phone_no', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
    ]