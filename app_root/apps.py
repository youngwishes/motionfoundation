from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppRootConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_root'
    label = 'root'
    verbose_name = _("general")
