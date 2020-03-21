#! /usr/bin/env sh

./manage.py migrate &&
./manage.py collectstatic &&
exec ./manage.py runserver 8080