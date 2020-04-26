FROM python:3.7.4

# アプリケーションのソースをバンドルする
COPY . /app
# ADD start.sh /app/start.sh

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING utf-8
ENV APP_PATH  /app

RUN pip install --upgrade pip
RUN pip install Django==3.0.3
RUN pip install flake8==3.7.9
RUN pip install ipython==7.10.1
RUN pip install mysqlclient==1.4.6
RUN pip install Pillow==6.2.2
RUN pip install uWSGI==2.0.18
RUN pip install django-cors-headers==3.2.1
