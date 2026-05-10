import time
from app.core.celery import celery



@celery.task
def send_email(email: str):
    time.sleep(5)

    return { "msg": f"{email}:success"}