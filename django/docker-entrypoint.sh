#!/bin/sh
cd /code/republikapi
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata data/initial.yaml
python manage.py runserver 0.0.0.0:8000