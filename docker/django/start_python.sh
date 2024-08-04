sleep 5
# gunicorn -c /app/app/uwsgi.ini melchior.wsgi:application
# gunicorn --access-logfile /app/logs/gunicorn/gunicorn.log --workers 3 --bind unix:/run/gunicorn.sock melchior.wsgi:application
gunicorn --access-logfile /app/logs/gunicorn/gunicorn.log --workers 3 --bind 0.0.0.0:8001 melchior.wsgi:application