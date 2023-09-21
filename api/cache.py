from typing import Any
from redis import Redis
from environs import Env

env = Env()
env.read_env()


class Cache:
    def __init__(self):
        self.redis = Redis(host=env.str('REDIS_HOST'), port=env.int('REDIS_PORT'), db=1, decode_responses=True)

    def set_cache(self, data: Any):
        return self.redis.set('data', data)

    def get_cache(self):
        return self.redis.get('data')

    def delete_cache(self):
        return self.redis.delete('data')
