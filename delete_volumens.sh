
#!/bin/bash

docker volume rm mlflow-minio-data
docker volume rm mlflow-posgresql-data

docker volume rm mlflow-production-data-logs
docker volume rm mlflow-production-models

docker volume rm mlflow-nginx-data-log
docker volume rm mlflow-data-logs