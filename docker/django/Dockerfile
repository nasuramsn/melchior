FROM python:3.12.4

# アプリケーションのソースをバンドルする
COPY ../../app /app
# ADD start.sh /app/start.sh

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING utf-8
ENV APP_PATH  /app

RUN pip install --upgrade pip
RUN pip install Django==5.0.7
RUN pip install flake8==7.0.0
RUN pip install ipython==8.26.0
RUN pip install mysqlclient==1.4.6
RUN pip install Pillow==10.4.0
RUN pip install uWSGI==2.0.26
RUN pip install django-cors-headers==4.4.0
RUN pip install coverage==7.6.0

RUN mkdir -p /var/www/html/
RUN mkdir -p /var/run/uwsgi/
RUN touch /var/run/uwsgi/melchior.sock
COPY ../../public /var/www/html/public
