#!/bin/bash

docker run --rm -v mlflow-nginx-data-log:/data busybox sh -c "rm -rf /data/*"
docker run --rm -v mlflow-posgresql-data:/data busybox sh -c "rm -rf /data/*"
docker run --rm -v mlflow-minio-data:/data busybox sh -c "rm -rf /data/*"
docker run --rm -v mlflow-minio-data:/data busybox sh -c "rm -rf /data/.minio.sys"
docker run --rm -v mlflow-data-logs:/data busybox sh -c "rm -rf /data/*"
docker run --rm -v mlflow-production-data-logs:/data busybox sh -c "rm -rf /data/*"
docker run --rm -v mlflow-production-models:/data busybox sh -c "rm -rf /data/*"