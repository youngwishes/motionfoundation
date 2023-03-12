from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class Partner(models.Model):
    """
    Партнёры.
    """
    name = models.CharField(_("name"), max_length=128, blank=True)
    logo = models.ImageField(verbose_name=_("logo"), upload_to='partners')
    partner_url = models.URLField("Ссылка на партнера")

    class Meta:
        verbose_name = _("partner")
        verbose_name_plural = _("partners")
        ordering = ("name",)

    def __str__(self):
        return self.name

    def clean(self):
        if not self.logo.name.endswith('.png' or '.svg'):
            raise ValidationError("Пожалуйста, загрузите .png формат файла.")


class ProjectType(models.Model):
    """
    Виды активностей.
    """
    name = models.CharField("тип проекта", max_length=256, db_index=True)

    class Meta:
        verbose_name = "тип проекта"
        verbose_name_plural = "типы проектов"
        ordering = ("name",)

    def __str__(self):
        return self.name


class ProjectPhoto(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name="photos")
    photo = models.ImageField("Фото проекта")


class Project(models.Model):
    """
    Проекты. Обязательное поле - название. Остальные - опционально.
    Если у проекта есть партнёры - заполните таблицу 'Партнёры' и добавьте соответствующих партнёров
    в эту таблицу.
    """
    name = models.CharField(_("name"), max_length=128, db_index=True)
    description = models.TextField(_("description"), blank=True)
    start_timestamp = models.DateTimeField(_("start timestamp"))
    end_timestamp = models.DateTimeField(_("end timestamp"))
    project_type = models.ForeignKey('ProjectType', on_delete=models.CASCADE, verbose_name="тип проекта")

    class Meta:
        verbose_name = _("project")
        verbose_name_plural = _("projects")
        ordering = ("start_timestamp",)

    def __str__(self):
        return self.name

    def clean(self):
        if self.start_timestamp >= self.end_timestamp:
            raise ValidationError(_("Start of the project cannot be later than its end"))
