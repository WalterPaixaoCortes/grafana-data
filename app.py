# -*- coding: utf-8 -*-
'''
    Main file to run the API
'''
from time import time
import os

import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import FileResponse


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
async def get_file(file: str, api_key: security_router.APIKey = security_router.Depends(security_router.get_api_key)):
    if os.path.isfile('data/{0}.csv'.format(file)):
        return FileResponse('data/{0}.csv'.format(file), media_type='text/csv')
    return None


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)
