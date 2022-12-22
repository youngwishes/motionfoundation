from django.contrib import admin, messages
from django.utils.translation import ngettext
from dvizhenie.core.loading import get_model

File = get_model('root', 'File')
AboutNKO = get_model('root', 'AboutTheFund')
MediaLinks = get_model('root', 'Contacts')


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


class AboutNKOAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'info']


class MediaLinksAdmin(admin.ModelAdmin):
    list_display = ['id', 'vk_url', 'ok_url', 'owner', 'phone', 'address']


admin.site.register(File, FileAdmin)
admin.site.register(AboutNKO, AboutNKOAdmin)
admin.site.register(MediaLinks, MediaLinksAdmin)
