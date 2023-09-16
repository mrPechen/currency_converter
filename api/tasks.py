from celery_dir.celery_app import task
from api.cache import Cache


@task.task
def update_cache():
    Cache().delete_cache()
