FROM ubuntu
FROM node:12.16.2

RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim"]

# アプリケーションディレクトリを作成する
WORKDIR /app

# アプリケーションの依存関係をインストールする
# ワイルドカードを使用して、package.json と package-lock.json の両方が確実にコピーされるようにします。
# 可能であれば (npm@5+)
COPY package*.json ./

RUN npm install -g npm && \
    npm install -g @vue/cli && \
    npm install vue-router && \
    npm install vuex --save

# 本番用にコードを作成している場合
# RUN npm install --only=production

# アプリケーションのソースをバンドルする
COPY . WORKDIR
# ADD start.sh /app/start.sh
