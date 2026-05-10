from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlalchemy import text
from app.api.v1.router import api_router
from app.middleware.register import register_middleware
from app.db.session import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Base.metadata.create_all(bind=engine)
    print("🚀 App startup: DB initialized")

    yield

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