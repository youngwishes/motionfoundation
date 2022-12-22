from django.db import models
from django.utils.translation import gettext_lazy as _


class News(models.Model):
    """
    Новости. Дата и время создания/обновления подставляются автоматически при создании/обновлении новости.
    Обязательное поле - заголовок. Остальные - опционально.
    """
    title = models.CharField(_("title"), max_length=128, db_index=True)
    description = models.TextField(_("description"), max_length=2048, blank=True)
    created_at = models.DateTimeField(_("Date and time of public news."), auto_now_add=True)
    updated_at = models.DateTimeField(_("Last update"), auto_now=True)
    short_description = models.TextField(_("short description"), max_length=512, blank=True)
    files = models.ManyToManyField('root.File', verbose_name=_("files"), related_name="news", blank=True)

    class Meta:
        verbose_name = _("news")
        verbose_name_plural = _("news")
        ordering = ("created_at",)

    def __str__(self):
        return self.title
