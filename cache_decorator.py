from functools import wraps
from time import perf_counter
import redis
import json


cache = redis.Redis(
        host='redis-18767.c17.us-east-1-4.ec2.cloud.redislabs.com',
        port=18767,
        password='pRPbp9UXd4bkPvOKvrNKJJxgSPSLqNIS'
    )

# cache key from request url
# https://admin.dev.placeexchange.com/api/v3/orgs/880940e1-5c71-4f1f-82eb-eab9ec8bb23a/deals/Ar_testDeal
# https://admin.dev.placeexchange.com/api/v3/deals/7f4c8e61-2a9b-4dd5-9ec7-ef82c1ad24e9


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
        # Generate the cache key from the function's arguments.
        cache_key = generate_cache_key(fn, *args)
        result = cache.get(cache_key)
        if result is None:
            # Run the function and cache the result for next time.
            value = fn(*args, **kwargs)
            value_json = json.dumps(value)
            cache.set(cache_key, value_json)
        else:
            # Skip the function entirely and use the cached value instead.
            value_json = result.decode('utf-8')
            value = json.loads(value_json)
        print(f"Display value from decorator {value}")
        return value

    return wrapper


def generate_cache_key(fn, *args):
    key_parts = [fn.__name__] + list(args)
    key = '-'.join(key_parts)
    return key


def memoize(fn):
    """
    memoize the cache
    """
    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]

    return inner
