from django.contrib import admin, messages
from django.utils.translation import ngettext

from dvizhenie.core.loading import get_model


FundEvent = get_model('events', 'FundEvent')
Address = get_model('events', 'Address')


class FundEventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'start_timestamp', 'end_timestamp', 'is_online']
    actions = ['make_as_online', 'make_as_offline']
    filter_horizontal = ('addresses',)
    fieldsets = (
        ('Название мероприятия', {
            'fields': ('name', 'description')
        }),
        ('Дата и время', {
            'classes': ('collapse',),
            'fields': ('start_timestamp', 'end_timestamp', 'addresses', ),
        }),
        ('Общее', {
            'classes': ('collapse',),
            'fields': ('is_online',),
        }),
        ('Фото', {
            'classes': ('collapse',),
            'fields': ('picture',)
        })
    )

    @admin.action(description='Перевести выбранные мероприятия в онлайн режим')
    def make_as_online(self, request, queryset):
        updated = queryset.update(is_online=True)
        self.message_user(request, ngettext(
            '%d event was successfully switched in online mode.',
            '%d events were successfully switched in online mode.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Перевести выбранные мероприятия в оффлайн режим')
    def make_as_offline(self, request, queryset):
        updated = queryset.update(is_online=False)
        self.message_user(request, ngettext(
            '%d event was successfully switched in offline mode.',
            '%d events were successfully switched in offline mode.',
            updated,
        ) % updated, messages.SUCCESS)


class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'address']


admin.site.register(FundEvent, FundEventAdmin)
admin.site.register(Address, AddressAdmin)
