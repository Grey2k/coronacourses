#! /usr/bin/env sh

./manage.py migrate &&
./manage.py collectstatic -c --noinput &&
exec ./manage.py runserver 8080