from celery import Celery

celery = Celery(
    "tasks",
    broker='redis://localhost:6379/0',
    include=["tasks.tasks"]
)
