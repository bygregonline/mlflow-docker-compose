#!/bin/bash


echo "Building containers"


docker build -f ./mlflow/Dockerfile ./mlflow  -t bygreg/mlflow-mlflow:v1
docker build -f ./nginx/Dockerfile ./nginx  -t bygreg/mlflow-nginx:v1
docker build -f ./minio/Dockerfile ./minio  -t bygreg/mlflow-minio:v1
docker build -f ./simple/Dockerfile ./simple  -t bygreg/mlflow-simple:v1
docker build -f ./production/Dockerfile ./production  -t bygreg/mlflow-production:v1