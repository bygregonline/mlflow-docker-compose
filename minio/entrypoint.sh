#!/bin/bash
printenv



minio server /data --console-address :$MINIO_WEB_UI_PORT &

sleep 10
mc alias set myminio http://localhost:9000 $MINIO_ROOT_USER $MINIO_ROOT_PASSWORD
mc mb myminio/mlflow-artifacts
sleep infinity

