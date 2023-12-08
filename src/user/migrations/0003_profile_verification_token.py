# Generated by Django 4.2.1 on 2023-06-23 13:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='verification_token',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]