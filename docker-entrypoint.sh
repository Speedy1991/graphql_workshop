#!/usr/bin/env bash

echo "Collect static"
python manage.py collectstatic --noinput

echo "Migrate"
python manage.py migrate

echo "Load data"
python manage.py loaddata assets/initial

chown -R www-data:www-data /app

uwsgi uwsgi.ini
