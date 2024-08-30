
import os
from fastapi import FastAPI
import mlflow.pyfunc
import numpy as np
import logging
from datetime import datetime
from time import time
from aniachi.systemUtils import Welcome as W
from fastapi.responses import PlainTextResponse
from fastapi.responses import JSONResponse
from typing import Dict, Any
from typing import List
from pydantic import BaseModel
import pytz


mexico_tz = pytz.timezone('America/Mexico_City')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Formato del log
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Handler para escribir logs en un archivo
file_handler = logging.FileHandler('/var/log/production/python/logger.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Opcional: también se puede agregar un StreamHandler para seguir mostrando los logs en la consola
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


app = FastAPI()

model_uri = os.environ['MLFLOW_MODEL_URI']
mlflow_uri = os.environ['MLFLOW_TRACKING_URI']
print(mlflow_uri)
print(model_uri)
# model = mlflow.pyfunc.load_model(model_uri)

# Carga el modelo desde MLflow


@app.post('/predict')
async def predict(data: List[float]):
    logger.info('predict')
    input_data = np.array(data).reshape(1, -1)
    logger.info(input_data)
    prediction = model.predict(input_data)
    return {'prediction': prediction.tolist()}


@app.get('/server')
async def server() -> JSONResponse:
    logger.info('server')
    data = W.get_fetchdata()
    return JSONResponse(content=data, status_code=200)


@app.get('/ping')
async def ping() -> PlainTextResponse:
    logger.info('ping')
    date = datetime.now(mexico_tz).strftime('%Y-%m-%d %H:%M:%S')
    return PlainTextResponse(f'pong {date}', status_code=200)


class SetupData(BaseModel):
    model: str


@app.post('/setup')
async def setup(data: SetupData) -> JSONResponse:
    logger.info('setup')
    logger.info(f'Data received: {data}')
    print(model)
    return JSONResponse(content={'message': 'done'}, status_code=200)


@app.post('/data')
async def data(data: Dict[str, Any]) -> JSONResponse:
    logger.info('setup')
    logger.info(f'Data received: {data}')
    date = datetime.now(mexico_tz).strftime('%Y-%m-%d %H:%M:%S')
    return JSONResponse({'content': data, 'time': date}, status_code=200)



# curl -X POST -H "Content-Type: application/json" -d '[9.1,  0.2 ,43.2,2,5,15,5,5,2,1,15]'  http://localhost:8000/predict
# payload

# [9.1,  0.2 ,43.2,2,5,15,5,5,2,1,15]