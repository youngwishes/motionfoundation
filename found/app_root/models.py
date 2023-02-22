from django.db import models
from django.utils.translation import gettext_lazy as _


class Gallery(models.Model):
    picture = models.ImageField("фото для галлереи")

    class Meta:
        verbose_name = "галлерея"
        verbose_name_plural = "галлерея"


class File(models.Model):
    """
    Все файлы, которые подгружаются на сайте.
    Будьте внимательны при удалении файлов, случайно можно удалить какой-либо использующийся файл.
    Если файл корпоративный - поставить флажок 'Документ фонда'.
    """
    file_field = models.FileField(
        _('file'), blank=True, upload_to='files_storage/'
    )
    is_fond_doc = models.BooleanField(_("is fond doc"), db_index=True, help_text=_("is file corporate or not"))
    capture = models.CharField(_("capture"), max_length=128, blank=True)

    def __str__(self):
        return self.capture

    class Meta:
        verbose_name = _("file")
        verbose_name_plural = _("files")


class Contacts(models.Model):
    """
    Контакты
    """
    vk_url = models.URLField(_("vk url"), max_length=200, blank=True)
    ok_url = models.URLField(_("odnoklassniki url"), max_length=200, blank=True)
    phone = models.CharField(_("phone number"), max_length=12, blank=True)
    owner = models.CharField(_('The fund owner'), max_length=128, blank=True)
    address = models.ForeignKey(
        'events.Address', verbose_name=_("address"), on_delete=models.CASCADE, blank=True
    )
    telegram = models.URLField(_("telegram"), max_length=200, blank=True)

    class Meta:
        verbose_name = _("contact")
        verbose_name_plural = _("contacts")

    def __str__(self):
        return self.owner
