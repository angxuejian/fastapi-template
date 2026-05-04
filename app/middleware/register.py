from fastapi import FastAPI
from app.middleware.request_log import request_log

def register_middleware(app: FastAPI):
    

    app.middleware("http")(request_log)
