# Generated by Django 4.2 on 2023-05-23 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0012_alter_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, default='This user is lazy and has nothing to say.', max_length=124, null=True),
        ),
    ]