# Generated by Django 3.2.19 on 2023-05-18 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_image',
        ),
    ]
