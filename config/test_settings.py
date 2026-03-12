"""
Test settings: use Postgres when DATABASE_URL is set (e.g. in CI).
"""
import os

from .settings import *  # noqa: F401, F403

if os.environ.get("DATABASE_URL"):
    import dj_database_url

    DATABASES["default"] = dj_database_url.config(conn_max_age=600)  # noqa: F405
else:
    DATABASES["default"] = {  # noqa: F405
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
