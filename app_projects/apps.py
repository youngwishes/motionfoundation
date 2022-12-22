from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppProjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_projects'
    label = 'projects'
    verbose_name = _("projects")
