FROM nginx:latest

# Instala apache2-utils para usar htpasswd
RUN apt-get update && apt-get install -y  \
    apache2-utils \
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
    iputils-ping \
    bat


# Copia la configuración de NGINX personalizada
COPY nginx.conf /etc/nginx/nginx.conf
RUN mkdir /etc/nginx/sites-available
RUN mkdir  -p /var/log/production/nginx/log/

# Script para crear usuario y contraseña
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# ENTRYPOINT ["/entrypoint.sh"]
# CMD ["nginx", "-g", "daemon off;"]
EXPOSE 9880