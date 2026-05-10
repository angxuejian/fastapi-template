from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from sqlalchemy import text
from app.api.v1.router import api_router
from app.middleware.register import register_middleware
from app.db.session import engine
from app.db.redis import create_redis


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 App startup: DB initialized")

    app.state.redis = create_redis()

    yield

    await app.state.redis.close()
    print("🛑 App shutdown")

app = FastAPI(lifespan=lifespan)

app.include_router(api_router, prefix='/api/v1')
register_middleware(app)

@app.get("/")
def read_root():
    return {"msg": "Hello FastAPI"}


@app.get("/health/db")
async def check_db():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            result.scalar()
        return {"status": "connected", "message": "数据库连接正常 ✅"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
@app.get('/redis-set')
async def redis_set(request: Request):

    redis = request.app.state.redis
    await redis.set("name", "xuejy", ex=60)
    return { "msg": "success" }

@app.get('/redis-get')
async def redis_set(request: Request):

    redis = request.app.state.redis
    name = await redis.get('name')
    return { "msg": name }