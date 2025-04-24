# redis_config.py
import redis.asyncio as redis

redis_client = redis.from_url("redis://redis:6379", decode_responses=True)
