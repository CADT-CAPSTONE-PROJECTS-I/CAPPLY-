# Generated by Django 4.2.1 on 2023-06-18 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0004_user_alter_scholarship_slug_alter_comment_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reply',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='slug',
            field=models.SlugField(default='vz6e3l12tyixh5gjtxmeibolputlfcev', unique=True),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
