#!/usr/bin/env bash

echo "Migrate"
python manage.py migrate

echo "Load data"
python manage.py loaddata assets/initial

echo "Start server"
python manage.py runserver 0.0.0.0:8000
