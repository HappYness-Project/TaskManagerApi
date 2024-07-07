# Generated by Django 5.0.6 on 2024-06-15 17:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_remove_task_users_taskcontainer_users'),
        ('users', '0003_usergroup_remove_user_default_user_group_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskcontainer',
            name='users',
        ),
        migrations.AddField(
            model_name='task',
            name='is_important',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='taskcontainer',
            name='user_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='containers', to='users.usergroup'),
        ),
    ]