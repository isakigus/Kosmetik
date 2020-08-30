from django.apps import AppConfig
from django.core.serializers import register_serializer


class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        register_serializer('yml', 'django.core.serializers.pyyaml')
