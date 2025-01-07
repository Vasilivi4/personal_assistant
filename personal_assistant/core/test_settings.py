from .settings import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "test_db",
        "USER": "postgres",
        "PASSWORD": "012601Nk",
        "HOST": "localhost",
        "PORT": "5432",
        "TEST": {
            "SERIALIZE": False,
            "NAME": None,  # Let Django create temp test db
        },
    }
}


# Disable migrations during tests
class DisableMigrations:
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


MIGRATION_MODULES = DisableMigrations()
