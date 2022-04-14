from django.apps import AppConfig

from simplemooc import accounts


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'simplemooc.accounts'
