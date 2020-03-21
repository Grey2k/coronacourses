#! /usr/bin/env sh

./manage.py migrate &&
exec ./manage.py runserver 8080