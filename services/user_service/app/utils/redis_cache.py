import redis
import json
from flask import current_app

def get_redis_client():
    return redis.StrictRedis(host="redis", port=6379, db=0)

def cache_set(key, value, timeout=3600):
    """Установите значение в кэше Redis."""
    client = get_redis_client()
    client.setex(key, timeout, json.dumps(value))

def cache_get(key):
    """Получите значение из кэша Redis."""
    client = get_redis_client()
    cached_value = client.get(key)
    if cached_value:
        return json.loads(cached_value)
    return None