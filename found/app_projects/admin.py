from django.contrib import admin
from django.utils.safestring import mark_safe
from dvizhenie.core.loading import get_model

Project = get_model('projects', 'Project')
Partner = get_model('projects', 'Partner')
ProjectPhoto = get_model('projects', 'ProjectPhoto')
ProjectType = get_model('projects', 'ProjectType')


class ProjectPhotosInline(admin.TabularInline):
    extra = 3
    model = ProjectPhoto


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'start_timestamp', 'end_timestamp', ]
    inlines = [ProjectPhotosInline]
    fieldsets = (
        ("Основная информация", {
            'fields': ('name', 'description', 'project_type')
        }),
        ('Дата и время', {
            'classes': ('collapse',),
            'fields': ('start_timestamp', 'end_timestamp')
        }),
    )


class ProjectTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class PartnerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_html_photo']

    @admin.decorators.display(description="Photo")
    def get_html_photo(self, instance):
        if instance.logo:
            return mark_safe(
                f"<a href='{instance.logo.url}'><img src='{instance.logo.url}' width=50></a>"
            )


admin.site.register(Project, ProjectAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(ProjectType, ProjectTypeAdmin)
