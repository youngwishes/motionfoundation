from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppQuestionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_questions'
    label = 'questions'
    verbose_name = _("questions")

