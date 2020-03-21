#! /usr/bin/env sh

./manage.py migrate &&
./manage.py collectstatic -c --noinput &&
exec ./manage.py runserver 0.0.0.0:8080