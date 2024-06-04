#!/bin/sh

# Exit the script if any command returns a non-true value
set -e

# Run migrations
python manage.py makemigrations
python manage.py migrate
python manage.py create_dummy_data

ADMIN_USERNAME=${DJANGO_ADMIN_USERNAME:-admin}
ADMIN_EMAIL=${DJANGO_ADMIN_EMAIL:-admin@example.com}
ADMIN_PASSWORD=${DJANGO_ADMIN_PASSWORD:-admin}

python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='${ADMIN_USERNAME}').exists():
    User.objects.create_superuser('${ADMIN_USERNAME}', '${ADMIN_EMAIL}', '${ADMIN_PASSWORD}')
END

# Execute the command passed to the script
exec "$@"