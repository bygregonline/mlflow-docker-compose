#!/bin/bash

printenv
uvicorn main:app  --host 0.0.0.0 --port 8000&
sleep infinity