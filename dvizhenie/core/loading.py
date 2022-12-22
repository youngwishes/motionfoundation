from importlib import import_module
from django.apps import apps as django_apps
from django.apps.config import MODELS_MODULE_NAME
from django.core.exceptions import AppRegistryNotReady


def get_model(app_label, model_name):
    try:
        return django_apps.get_model(app_label, model_name)
    except AppRegistryNotReady:
        if django_apps.apps_ready and django_apps.models_ready:
            app_config = django_apps.get_app_config(app_label)
            import_module('%s.%s' % (app_config.name, MODELS_MODULE_NAME))
            return django_apps.get_registered_model(app_label, model_name)
        else:
            raise
