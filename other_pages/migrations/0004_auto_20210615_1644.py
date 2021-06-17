# Generated by Django 3.2.4 on 2021-06-15 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('other_pages', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResearchTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('post', models.CharField(blank=True, max_length=200)),
                ('email', models.CharField(blank=True, max_length=200)),
                ('phone_no', models.CharField(blank=True, max_length=200)),
                ('url', models.CharField(blank=True, max_length=200)),
                ('remarks', models.TextField(blank=True, max_length=200)),
                ('category', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='organiztion_name',
            new_name='organization_name',
        ),
    ]
