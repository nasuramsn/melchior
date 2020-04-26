FROM nginx:1.11.7

# 設定ファイル
ADD ./nginx/conf/default.conf /etc/nginx/conf.d/default.conf
ADD ./nginx/conf//default.conf /etc/nginx/sites-available/default
ADD ./nginx/conf//default.conf /etc/nginx/sites-enabled/default
ADD ./nginx/uwsgi_params /etc/nginx/uwsgi_params

RUN mkdir /static
RUN mkdir /static/admin
RUN mkdir /var/www
RUN mkdir /var/www/dist
RUN mkdir /var/www/static

COPY ./static/admin /static/admin