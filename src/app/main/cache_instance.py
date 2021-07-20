import redis

def redis_connection():
    cache = redis.Redis(host='cache',
                    port=6379,
                    charset='utf-8',
                    decode_responses=True)
    return cache