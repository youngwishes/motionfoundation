from django.db import models
from django.utils.translation import gettext_lazy as _


class Question(models.Model):
    """
    Наиболее часто встречающиеся вопросы. Отображаются на главной странице фонда внизу.
    """
    question = models.CharField(_("question"), max_length=256)
    answer = models.TextField(_("answer"))

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = _("question")
        verbose_name_plural = _("questions")
