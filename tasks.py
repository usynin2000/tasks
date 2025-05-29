from celery import Celery

import time

app = Celery(
    "demo",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@app.task
def add(x, y):
    time.sleep(5)  # Симулируем долгую операцию
    return x + y