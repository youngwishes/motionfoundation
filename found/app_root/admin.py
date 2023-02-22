from django.contrib import admin, messages
from django.utils.safestring import mark_safe
from django.utils.translation import ngettext
from dvizhenie.core.loading import get_model

File = get_model('root', 'File')
MediaLinks = get_model('root', 'Contacts')
Gallery = get_model('root', 'Gallery')


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_html_photo']

    @admin.decorators.display(description="Photo")
    def get_html_photo(self, instance):
        if instance.picture:
            return mark_safe(
                f"<a href='{instance.picture.url}'>"
                f"<img src='{instance.picture.url}' width=150>"
                f"</a>"
            )


class FileAdmin(admin.ModelAdmin):
    list_display = ['id', 'capture', 'file_field', 'is_fond_doc']
    actions = ('make_as_corp', 'make_as_non_corp')

    @admin.action(description='Сделать файлы корпоративными')
    def make_as_corp(self, request, queryset):
        updated = queryset.update(is_fond_doc=True)
        self.message_user(request, ngettext(
            '%d file was successfully marked as corporative.',
            '%d files were successfully marked as corporative.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Сделать файлы некорпоративными')
    def make_as_non_corp(self, request, queryset):
        updated = queryset.update(is_fond_doc=False)
        self.message_user(request, ngettext(
            '%d file was successfully marked as not corporative.',
            '%d files were successfully marked as not corporative.',
            updated,
        ) % updated, messages.SUCCESS)


class MediaLinksAdmin(admin.ModelAdmin):
    list_display = ['id', 'vk_url', 'ok_url', 'owner', 'phone', 'address']


admin.site.register(File, FileAdmin)
admin.site.register(MediaLinks, MediaLinksAdmin)
admin.site.register(Gallery, GalleryAdmin)
