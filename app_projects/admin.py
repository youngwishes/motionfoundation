from django.contrib import admin
from django.utils.translation import ngettext

from dvizhenie.core.loading import get_model

from django.contrib import messages

Project = get_model('projects', 'Project')
Partner = get_model('projects', 'Partner')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'start_timestamp', 'end_timestamp', 'is_finished']
    actions = ('make_as_finished', 'make_as_in_proc')
    filter_horizontal = ('files', 'partners')
    fieldsets = (
        ("Основная информация", {
            'fields': ('name', 'description',)
        }),
        ('Дата и время', {
            'classes': ('collapse',),
            'fields': ('start_timestamp', 'end_timestamp', 'is_finished')
        }),
        ('Партнеры', {
            'classes': ('collapse',),
            'fields': ('partners',)
        }),
        ('Файлы', {
            'classes': ('collapse',),
            'fields': ('files',)
        }),

    )

    @admin.action(description='Сделать выбранные проекты законченными')
    def make_as_finished(self, request, queryset):
        updated = queryset.update(is_finished=True)
        self.message_user(request, ngettext(
            '%d project was successfully marked as finished.',
            '%d projects were successfully marked as finished.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Сделать выбранные проекты незаконченными')
    def make_as_in_proc(self, request, queryset):
        updated = queryset.update(is_finished=False)
        self.message_user(request, ngettext(
            '%d project was successfully marked as in process.',
            '%d projects were successfully marked as in process.',
            updated,
        ) % updated, messages.SUCCESS)


class PartnerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Partner, PartnerAdmin)
