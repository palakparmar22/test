# Generated by Django 5.1 on 2024-08-30 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_user_is_masteruser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]
