# Generated by Django 5.0.6 on 2024-06-25 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_usergroup_remove_user_default_user_group_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_group',
        ),
        migrations.AddField(
            model_name='user',
            name='user_groups',
            field=models.ManyToManyField(related_name='group_users', to='users.usergroup'),
        ),
    ]