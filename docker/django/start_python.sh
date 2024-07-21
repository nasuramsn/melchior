sleep 5
uwsgi --ini /app/app/uwsgi.ini
sleep 5
uwsgi --socket :8001 --wsgi-file /app/app/melchior/wsgi.py -b 65535