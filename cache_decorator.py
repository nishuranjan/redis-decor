from functools import wraps
from time import perf_counter
import redis
import json


cache = redis.Redis(
        host='<redis endpoint>',
        port=<redis port>,
        password='<enter ur redis password>'
    )


def test_redis():
    cache.set('foo', 'bar')
    value = cache.get('foo')
    print(value)

# testing the cache
# test_redis()


def cached(fn):
    """Decorator that caches the results of the function call."""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # Get the cache key from the function's arguments.
        cache_key = get_cache_key(fn, *args)
        result = cache.get(cache_key)
        if result is None:
            # Run the function and cache the result for next time.
            value = fn(*args, **kwargs)
            value_json = json.dumps(value)
            cache.set(cache_key, value_json, 120)
        else:
            # Skip the function entirely and use the cached value instead.
            value_json = result.decode('utf-8')
            value = json.loads(value_json)
        print(f"Display value from decorator {value}")
        return value

    return wrapper


def invalidate_cached(fn):
    """Decorator that invalidate caches the results of the function call."""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # Get the cache key from the function's arguments.
        cache_key = get_cache_key(fn, *args)
        result = cache.get(cache_key)
        # print("result {0}".format(result))
        value = "Cache evicted for key {0} - in process".format(cache_key)
        if result:
            # Run the function and cache the result for next time.
            cache.delete(cache_key)
            value = "Cache evicted for key {0} - completed".format(cache_key)
        else:
            value = "Cache key not found in redis"
        print(value)
        return value

    return wrapper


def get_cache_key(fn, *args):
    key_parts = [fn.__name__] + list(args)
    key = '-'.join(key_parts)
    return key
