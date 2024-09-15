# ベースイメージとして python:3.9.6-slim-buster を使用
FROM python:3.9.6-slim-buster

# 作業ディレクトリを設定
WORKDIR /app

# 必要に応じてシステムのパッケージを更新（オプション）
RUN apt-get update && apt-get upgrade -y

# 必要なシステムパッケージをインストール
RUN apt-get install -y build-essential linux-headers-amd64

# Python パッケージをインストール
# requirements.txt がある場合は、それを利用して依存パッケージをインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコンテナにコピー
COPY . .
