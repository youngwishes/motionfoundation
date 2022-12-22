from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class Partner(models.Model):
    """
    Партнёры.
    """
    name = models.CharField(_("name"), max_length=128, blank=True)
    logo = models.ForeignKey(
        'root.File', verbose_name=_("logo"), blank=True, related_name="partner", on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("partner")
        verbose_name_plural = _("partners")
        ordering = ("name",)

    def __str__(self):
        return self.name


class Project(models.Model):
    """
    Проекты. Обязательное поле - название. Остальные - опционально.
    Если у проекта есть партнёры - заполните таблицу 'Партнёры' и добавьте соответствующих партнёров
    в эту таблицу.
    """
    name = models.CharField(_("name"), max_length=128, db_index=True)
    description = models.TextField(_("description"), max_length=2048, blank=True)
    start_timestamp = models.DateTimeField(_("start timestamp"))
    end_timestamp = models.DateTimeField(_("end timestamp"))

    is_finished = models.BooleanField(
        _("is finished"), db_index=True, help_text=_("Is this project has finished?")
    )

    partners = models.ManyToManyField(
        Partner, verbose_name=_("partners"), related_name="projects", blank=True
    )

    files = models.ManyToManyField(
        'root.File', verbose_name=_("files"), related_name="projects", blank=True
    )

    class Meta:
        verbose_name = _("project")
        verbose_name_plural = _("projects")
        ordering = ("start_timestamp",)

    def __str__(self):
        return self.name

    def clean(self):
        if self.start_timestamp >= self.end_timestamp:
            raise ValidationError(_("Start of the project cannot be later than its end"))
