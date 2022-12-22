from django.db import models
from django.utils.translation import gettext_lazy as _


class ActivityType(models.Model):
    """
    Виды активностей.
    """
    name = models.CharField(_("activity type"), max_length=256, db_index=True)

    class Meta:
        verbose_name = _("activity type")
        verbose_name_plural = _("activities types")
        ordering = ("name",)

    def __str__(self):
        return self.name


class Activity(models.Model):
    """
    Активность, обязательные атрибуты: название, вид активности. Остальные - опционально.
    """
    name = models.CharField(_("activity name"), max_length=128, db_index=True)
    description = models.TextField(_("activity description"), max_length=256, blank=True)
    activity_type = models.ForeignKey(
        ActivityType, verbose_name=_("activity type"), related_name="activity", on_delete=models.CASCADE
    )
    files = models.ManyToManyField('root.File', verbose_name=_("files"), related_name="activities")

    class Meta:
        verbose_name = _("activity")
        verbose_name_plural = _("activities")
        ordering = ("name",)

    def __str__(self):
        return self.name
