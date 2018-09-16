#!/bin/sh
cd /var/www/
flask db init
flask db migrate
flask db upgrade
uwsgi --ini /config/uwsgi/uwsgi.ini 
