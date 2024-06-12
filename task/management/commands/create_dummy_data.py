from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from task.models import Task, TaskContainer, TaskCategory, Priority
from users.models import UserGroup
from faker import Faker
from datetime import datetime, timedelta
import random

class Command(BaseCommand):
    help = 'Create dummy data for Task and TaskContainer models'

    def handle(self, *args, **kwargs):
        fake = Faker()
        User = get_user_model()

        # Create dummy user groups
        user_groups = []
        for _ in range(5):
            user_group = UserGroup.objects.create(
                group_name=fake.company(),
                group_type=random.choice(['type1', 'type2'])
            )
            user_groups.append(user_group)
        self.stdout.write(self.style.SUCCESS('Successfully created dummy user groups'))

        # Create dummy users and assign them to user groups
        for _ in range(10):
            user_group = random.choice(user_groups)
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password123',
                user_group=user_group
            )
        self.stdout.write(self.style.SUCCESS('Successfully created dummy users'))

        # Create dummy tasks
        task_ids = []
        for _ in range(50):
            task = Task.objects.create(
                task_name=fake.sentence(nb_words=6),
                task_desc=fake.paragraph(),
                target_date=datetime.now() + timedelta(days=random.randint(1, 365)),
                is_completed=fake.boolean(),
                priority=random.choice([Priority.URGENT, Priority.NORMAL, Priority.LOW]),
                task_category=random.choice([TaskCategory.GROCERY, TaskCategory.TRAVEL, TaskCategory.LEISURE, TaskCategory.WORK])
            )
            task_ids.append(task.task_id)
        self.stdout.write(self.style.SUCCESS('Successfully created dummy tasks'))

        # Create dummy task containers
        for _ in range(10):
            user_group = random.choice(user_groups)
            container = TaskContainer.objects.create(
                container_name=fake.word(),
                user_group=user_group
            )
            # Add random tasks to the container
            tasks_to_add = Task.objects.filter(task_id__in=random.sample(task_ids, random.randint(1, 10)))
            container.tasks.set(tasks_to_add)

        self.stdout.write(self.style.SUCCESS('Successfully created dummy task containers'))
