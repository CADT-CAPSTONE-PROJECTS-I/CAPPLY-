# Generated by Django 4.2 on 2023-05-21 16:17

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.TextField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='user/profile_pictures/', verbose_name=django.contrib.auth.models.User),
        ),
        migrations.AddField(
            model_name='profile',
            name='school',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=124, null=True),
        ),
    ]
