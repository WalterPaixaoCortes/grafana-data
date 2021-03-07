# -*- coding: utf-8 -*-
'''
    Main file to run the API
'''
import base64
import json
from time import time

import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.gzip import GZipMiddleware

import config
from routers import security_router

app = FastAPI(title="Grafana Data REST API")
app.add_middleware(GZipMiddleware, minimum_size=1000)


@app.middleware("http")
async def remove_file_before_leave(request: Request, call_next):
    start_time = time()
    response = await call_next(request)
    process_time = time()
    response.headers["X-Process-Time"] = str(process_time - start_time)
    return response


@app.get("/v1/{file}", tags=["Version 1"])
async def get_pokemon_by_id(file: str, api_key: security_router.APIKey = security_router.Depends(security_router.get_api_key)):
    record = ''
    try:
        fil = open('data/{0}.csv'.format(file), 'r').readlines()
        data = '\n'.join(fil)
        record = data
    except:
        record = 'Error\nError loading file.'
    return record


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)
