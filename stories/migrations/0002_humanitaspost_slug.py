# Generated by Django 3.2.19 on 2023-05-12 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='humanitaspost',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]
