from django.db import models
from django.utils.translation import gettext_lazy as _


class News(models.Model):
    """
    Новости. Дата и время создания/обновления подставляются автоматически при создании/обновлении новости.
    Обязательное поле - заголовок. Остальные - опционально.
    """
    title = models.CharField(_("title"), max_length=128, db_index=True)
    description = models.TextField(_("description"), blank=True)
    created_at = models.DateTimeField(_("Date and time of public news."), auto_now_add=True)
    updated_at = models.DateTimeField(_("Last update"), auto_now=True)
    picture = models.ImageField("фото")

    class Meta:
        verbose_name = _("news")
        verbose_name_plural = _("news")
        ordering = ("created_at",)

    def __str__(self):
        return self.title
