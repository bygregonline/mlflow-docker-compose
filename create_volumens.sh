
#!/bin/bash

docker volume create mlflow-minio-data
docker volume create mlflow-posgresql-data

docker volume create mlflow-production-data-logs
docker volume create mlflow-production-models

docker volume create mlflow-nginx-data-log
docker volume create mlflow-data-logs