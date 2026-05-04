from fastapi import FastAPI
from app.api.v1.router import api_router
from app.middleware.register import register_middleware

app = FastAPI()

app.include_router(api_router, prefix='/api/v1')
register_middleware(app)

@app.get("/")
def read_root():
    return {"msg": "Hello FastAPI"}