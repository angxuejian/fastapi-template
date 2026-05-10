from celery import Celery
from app.core.config import settings

celery = Celery(
    "worker",
    broker=settings.REDIS_URL + '/0',
    backend=settings.REDIS_URL + '/1'
)

import app.tasks.email