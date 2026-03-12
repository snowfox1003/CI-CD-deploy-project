"""Minimal smoke tests so CI test job runs and passes."""

from django.conf import settings


def test_django_settings_loaded():
    """Django test settings are applied."""
    assert settings.SECRET_KEY is not None
    assert isinstance(settings.INSTALLED_APPS, list)


def test_database_configured():
    """Default database is configured."""
    assert "default" in settings.DATABASES
    assert settings.DATABASES["default"]["ENGINE"] in (
        "django.db.backends.postgresql",
        "django.db.backends.sqlite3",
    )
