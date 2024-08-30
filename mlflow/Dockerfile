FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    postgresql-client \
    curl \
    wget \
    git \
    nmap \
    htop \
    procps \
    zip \
    jq \
    bat \
    micro \
    nginx \
    neofetch \
    iputils-ping \
    bind9-dnsutils







RUN pip install --upgrade pip
RUN pip install mlflow psycopg2 psycopg2-binary pandas  minio rich boto3

# Exponer el puerto en el que MLflow se ejecutará
EXPOSE 5555

# Comando para iniciar MLflow
# CMD ["mlflow", "server", "--host", "0.0.0.0"]

