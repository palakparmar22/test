# Generated by Django 5.0.3 on 2024-04-23 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_remove_user_is_candidate_remove_user_is_hr_user_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
        migrations.AddField(
            model_name='user',
            name='is_candidate',
            field=models.BooleanField(default=False, verbose_name='Is candidate'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_employee',
            field=models.BooleanField(default=False, verbose_name='Is employee'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_hr',
            field=models.BooleanField(default=False, verbose_name='Is hr'),
        ),
    ]
