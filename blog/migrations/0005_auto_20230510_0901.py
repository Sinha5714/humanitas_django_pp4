# Generated by Django 3.2.19 on 2023-05-10 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_humanitaspost_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='humanitaspost',
            options={'ordering': ['-updated_on']},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
        migrations.RemoveField(
            model_name='humanitaspost',
            name='likes',
        ),
        migrations.AlterField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=400),
        ),
    ]
