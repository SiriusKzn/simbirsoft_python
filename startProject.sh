#!/bin/bash
echo 'Wait....'
docker-compose build
docker-compose up -d
sleep 10s
docker-compose stop 
docker-compose run web python manage.py migrate
docker-compose start