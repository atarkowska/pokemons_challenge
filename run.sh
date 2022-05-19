#!/bin/bash

echo "DB startup..."
until python manage.py check --database default; do
  >&2 echo "PSQL is unavailable - sleeping"
  sleep 5
done
>&2 echo "PSQL now accepts connections, creating database..."


python manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@mlocalhost', 'password')" | python manage.py shell
python manage.py runserver 0.0.0.0:8000