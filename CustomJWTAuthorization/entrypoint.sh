#!/bin/bash
set -e

echo "Applying database migrations..."
python manage.py migrate --noinput

echo "Creating superuser if not exists..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); \
User.objects.filter(username='admin').exists() or \
    User.objects.create_superuser(email='admin@admin.com', username='admin', password='adminpass1337')" | python manage.py shell

exec "$@"