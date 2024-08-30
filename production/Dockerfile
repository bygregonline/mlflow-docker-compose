# Usa una imagen base de Python
FROM python:3.11-slim
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    wget \
    git \
    nmap \
    htop \
    procps \
    zip \
    jq \
    micro \
    bind9-dnsutils \
    neofetch \
    iputils-ping \
    nano \
    bat



WORKDIR /app

RUN mkdir  -p /var/log/production/python/
RUN mkdir  -p /

COPY requirements.txt .
COPY main.py .
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh



RUN pip install --no-cache-dir -r requirements.txt



# RUN apt-get install -y iputils-ping


EXPOSE 8000