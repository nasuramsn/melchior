FROM python:3.10.8


WORKDIR /app

RUN apt-get update && \
    curl -sL https://deb.nodesource.com/setup_12.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g npm@6.14.16 && \
    npm install -g yarn

COPY . /app

ENV PYTHONUNBUFFERED 1
ENV APP_PATH  /app

RUN pip install --upgrade pip && \
    echo ----------------------- the workdir src contains: && \
    ls && \
    echo ----------------------- Now installing requirements... && \
    pip install -r ./app/requirements.txt
