# Generated by Django 3.2.19 on 2023-05-20 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_remove_profile_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('message_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(default='', max_length=100)),
                ('message', models.TextField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
