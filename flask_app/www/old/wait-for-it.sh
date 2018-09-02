#!/bin/bash
until python /var/www/wait.py --host mysql_ctr --port 3306 ; do
  >&2 echo "mysql is unavailable - sleeping"
  sleep 1
done
>&2 echo "mysql is up - executing command"
# exec python /var/www/first.py && uwsgi --ini ${container_mountpoint_uwsgi}uwsgi.ini