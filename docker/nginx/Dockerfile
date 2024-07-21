FROM nginx:1.27.0

# 設定ファイル
ADD ./docker/nginx/conf/default.conf /etc/nginx/conf.d/default.conf
ADD ./docker/nginx/conf/default.conf /etc/nginx/sites-available/default
ADD ./docker/nginx/conf/default.conf /etc/nginx/sites-enabled/default
ADD ./docker/nginx/uwsgi_params /etc/nginx/uwsgi_params

RUN mkdir /static
RUN mkdir /static/admin
RUN mkdir /var/www
RUN mkdir /var/www/dist
RUN mkdir /var/www/static

COPY ./static/admin /static/admin