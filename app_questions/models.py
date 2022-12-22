from django.db import models
from django.utils.translation import gettext_lazy as _


class Question(models.Model):
    """
    Наиболее часто встречающиеся вопросы. Отображаются на главной странице фонда внизу.
    """
    question = models.CharField(_("question"), max_length=256)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = _("question")
        verbose_name_plural = _("questions")


class Answer(models.Model):
    """
    Ответы на вопросы.
    """
    answer = models.TextField(_("answer"))
    question = models.ForeignKey(Question, verbose_name=_("question"), on_delete=models.CASCADE, related_name='answer')

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = _("answer")
        verbose_name_plural = _("answers")
        order_with_respect_to = 'question'
