# Generated by Django 4.2 on 2023-05-23 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0011_alter_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='This user is lazy and has nothing to say.', max_length=124, null=True),
        ),
    ]