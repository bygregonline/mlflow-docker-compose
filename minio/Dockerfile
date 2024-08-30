
FROM ubuntu:22.04
WORKDIR app
# Actualiza el sistema e instala dependencias necesarias
RUN apt-get update && apt-get install -y \
    wget \
    curl \
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
    micro \
    bind9-dnsutils \
    neofetch \
    ca-certificates \
    bat


# Descarga e instala MinIO
RUN wget https://dl.min.io/server/minio/release/linux-amd64/minio \
    && chmod +x minio \
    && mv minio /usr/local/bin/

RUN wget https://dl.min.io/client/mc/release/linux-amd64/mc \
    && chmod +x mc \
    && mv mc /usr/local/bin





COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
# Crea un directorio para almacenar los datos
RUN mkdir -p /data

# Exponer los puertos 9000 y 9001
EXPOSE 9000 9001 42065


