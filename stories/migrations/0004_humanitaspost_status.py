# Generated by Django 3.2.19 on 2023-05-12 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_alter_humanitaspost_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='humanitaspost',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=1),
        ),
    ]
