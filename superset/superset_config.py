import os
import redis
from flask_caching import Cache

# -----------------------------------------------------------------------------
# Database
# Build SQLALCHEMY_DATABASE_URI from your .env
# -----------------------------------------------------------------------------
SQLALCHEMY_DATABASE_URI = (
    f"{os.environ['DATABASE_DIALECT']}+psycopg2://"
    f"{os.environ['DATABASE_USER']}:"
    f"{os.environ['DATABASE_PASSWORD']}@"
    f"{os.environ['DATABASE_HOST']}:"
    f"{os.environ['DATABASE_PORT']}/"
    f"{os.environ['DATABASE_DB']}"
)

# ---------------------------------------------------------------------
# SECRET_KEY: used for session signing and encrypted field decryption.
# (You can override by setting SECRET_KEY in your .env)
# ---------------------------------------------------------------------
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "LrKNhNDps82/5j1qV0FE51E6VlDpl2jedeGAcrZlsUkaKwCHySKSy8hJ",
)

# ---------------------------------------------------------------------
# Flask-Limiter (rate-limiting)
# ---------------------------------------------------------------------
RATELIMIT_ENABLED = True
RATELIMIT_STORAGE_URI = "redis://superset_cache:6379/0"
RATELIMIT_STRATEGY = "fixed-window"

# ---------------------------------------------------------------------
# Results Caching (queries & chart fragments)
# ---------------------------------------------------------------------
CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_KEY_PREFIX": "superset_",
    "CACHE_REDIS_URL": "redis://superset_cache:6379/1",
}

# ---------------------------------------------------------------------
# Celery (async query execution)
# ---------------------------------------------------------------------
CELERY_BROKER_URL = "redis://superset_cache:6379/2"
CELERY_RESULT_BACKEND = "redis://superset_cache:6379/3"

# ---------------------------------------------------------------------
# Session storage (optional)
# ---------------------------------------------------------------------
SESSION_TYPE = "redis"
SESSION_REDIS = redis.StrictRedis(
    host="superset_cache", port=6379, db=4, decode_responses=True
)
