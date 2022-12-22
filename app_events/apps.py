from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppEventsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_events'
    label = 'events'
    verbose_name = _("events")
