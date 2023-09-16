from celery import Celery
from environs import Env
from celery.schedules import crontab

env = Env()
env.read_env()

task = Celery('celery_app',
              broker=f"amqp://{env.str('RABBITMQ_DEFAULT_USER')}:{env.str('RABBITMQ_DEFAULT_PASS')}@{env.str('RABBITMQ_HOST')}:{env.str('RABBITMQ_PORT')}//")

task.conf.beat_schedule = {
    'update_cache_every_day': {
        'task': 'api.tasks.update_cache',
        'schedule': crontab(hour='11', minute='31'),
    },
}
task.conf.timezone = 'Europe/Moscow'
task.autodiscover_tasks()
