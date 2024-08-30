#!/bin/bash

# Crea el archivo .htpasswd con las credenciales proporcionadas
if [[ -n "$BASIC_AUTH_USERNAME" && -n "$BASIC_AUTH_PASSWORD" ]]; then
    htpasswd -bc /etc/nginx/.htpasswd $BASIC_AUTH_USERNAME $BASIC_AUTH_PASSWORD
fi
echo "NGINX: $@"
echo $BASIC_AUTH_USERNAME
echo $BASIC_AUTH_PASSWORD
service nginx start